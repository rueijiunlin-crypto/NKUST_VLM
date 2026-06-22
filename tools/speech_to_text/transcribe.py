"""Speech-to-Text tool based on faster-whisper."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable


SUPPORTED_AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}
DEFAULT_MODEL = "large-v3-turbo"
DEFAULT_LANGUAGE = "zh"


def parse_args() -> argparse.Namespace:
    """解析命令列參數。"""
    parser = argparse.ArgumentParser(
        description="使用 faster-whisper 將音檔轉成文字逐字稿。"
    )
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--audio", type=Path, help="指定單一音檔路徑。")
    source_group.add_argument("--input-dir", type=Path, help="指定音檔資料夾並批次轉錄。")

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("transcripts"),
        help="輸出逐字稿資料夾，預設為 transcripts。",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        choices=("small", "medium", "large-v3", "large-v3-turbo"),
        help=f"Whisper 模型名稱，預設為 {DEFAULT_MODEL}。",
    )
    parser.add_argument(
        "--language",
        default=DEFAULT_LANGUAGE,
        help="辨識語言，預設 zh；指定 auto 時交由模型自動偵測。",
    )
    parser.add_argument(
        "--timestamps",
        action="store_true",
        help="輸出逐段時間戳。",
    )
    parser.add_argument(
        "--device",
        default="auto",
        choices=("auto", "cuda", "cpu"),
        help="指定推論裝置，預設 auto。",
    )
    parser.add_argument(
        "--compute-type",
        default="auto",
        choices=("auto", "float16", "int8", "int8_float16"),
        help="指定 faster-whisper compute_type，預設 auto。",
    )

    vad_group = parser.add_mutually_exclusive_group()
    vad_group.add_argument(
        "--vad",
        dest="vad_filter",
        action="store_true",
        default=True,
        help="啟用 VAD（語音活動偵測），預設啟用。",
    )
    vad_group.add_argument(
        "--no-vad",
        dest="vad_filter",
        action="store_false",
        help="關閉 VAD，避免內容被靜音過濾切掉。",
    )
    return parser.parse_args()


def format_timestamp(seconds: float) -> str:
    """將秒數轉成 HH:MM:SS.xx 格式。"""
    if seconds < 0:
        seconds = 0
    centiseconds = int(round(seconds * 100))
    hours, remainder = divmod(centiseconds, 3600 * 100)
    minutes, remainder = divmod(remainder, 60 * 100)
    secs, centis = divmod(remainder, 100)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{centis:02d}"


def resolve_device_and_compute_type(device: str, compute_type: str) -> tuple[str, str]:
    """依裝置決定 faster-whisper compute_type。"""
    if compute_type != "auto":
        return device, compute_type
    if device == "cpu":
        return device, "int8"
    return device, "float16"


def collect_audio_files(audio: Path | None, input_dir: Path | None) -> list[Path]:
    """收集單一或批次音檔路徑。"""
    if audio is not None:
        audio_path = audio.expanduser()
        if not audio_path.exists():
            raise FileNotFoundError(f"找不到音檔：{audio_path}")
        if not audio_path.is_file():
            raise ValueError(f"--audio 必須指向單一檔案：{audio_path}")
        if audio_path.suffix.lower() not in SUPPORTED_AUDIO_EXTENSIONS:
            supported = ", ".join(sorted(SUPPORTED_AUDIO_EXTENSIONS))
            raise ValueError(f"不支援的音訊格式：{audio_path.suffix}；支援格式：{supported}")
        return [audio_path]

    if input_dir is None:
        raise ValueError("請指定 --audio 或 --input-dir。")

    root = input_dir.expanduser()
    if not root.exists():
        raise FileNotFoundError(f"找不到 input-dir：{root}")
    if not root.is_dir():
        raise ValueError(f"--input-dir 必須指向資料夾：{root}")

    files = sorted(
        path for path in root.rglob("*") if path.suffix.lower() in SUPPORTED_AUDIO_EXTENSIONS
    )
    if not files:
        supported = ", ".join(sorted(SUPPORTED_AUDIO_EXTENSIONS))
        raise FileNotFoundError(f"{root} 內沒有找到支援格式音檔。支援格式：{supported}")
    return files


def _cuda_failure_hint(error: Exception) -> str:
    return (
        "CUDA 初始化或模型載入失敗，將改用 CPU。可能原因包含：\n"
        "- NVIDIA driver（NVIDIA 驅動程式）尚未安裝或版本不符。\n"
        "- CUDA Runtime（CUDA 執行環境）缺失。\n"
        "- cuDNN（深度神經網路加速函式庫）缺失。\n"
        "- faster-whisper 或 ctranslate2 依賴不完整。\n"
        "- Python 虛擬環境套件安裝錯誤。\n"
        f"原始錯誤：{error}"
    )


def load_model(model_size_or_path: str, device: str, compute_type: str):
    """載入 WhisperModel，必要時從 CUDA fallback 到 CPU。"""
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError(
            "尚未安裝 faster-whisper。請先執行：pip install -r requirements.txt"
        ) from exc

    candidate_devices = ["cuda", "cpu"] if device in {"auto", "cuda"} else ["cpu"]
    last_error: Exception | None = None

    for candidate in candidate_devices:
        resolved_device, resolved_compute_type = resolve_device_and_compute_type(
            candidate, compute_type
        )
        print(
            f"[INFO] 載入模型：model={model_size_or_path}, "
            f"device={resolved_device}, compute_type={resolved_compute_type}"
        )
        try:
            model = WhisperModel(
                model_size_or_path,
                device=resolved_device,
                compute_type=resolved_compute_type,
            )
            return model, resolved_device, resolved_compute_type
        except Exception as exc:  # faster-whisper 會依系統拋出不同例外型別。
            last_error = exc
            if candidate == "cuda" and "cpu" in candidate_devices:
                print(f"[WARN] {_cuda_failure_hint(exc)}", file=sys.stderr)
                continue
            raise RuntimeError(f"模型載入失敗：{exc}") from exc

    raise RuntimeError(f"模型載入失敗：{last_error}")


def transcribe_audio(
    model,
    audio_path: Path,
    language: str,
    vad_filter: bool,
) -> tuple[list, object]:
    """執行單一音檔轉錄。"""
    transcribe_kwargs = {"vad_filter": vad_filter}
    if language.lower() != "auto":
        transcribe_kwargs["language"] = language

    print(f"[INFO] 開始轉錄：{audio_path}")
    segments, info = model.transcribe(str(audio_path), **transcribe_kwargs)
    return list(segments), info


def save_transcript(
    segments: Iterable,
    output_path: Path,
    timestamps: bool,
) -> None:
    """儲存 txt 逐字稿。"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    for segment in segments:
        text = segment.text.strip()
        if not text:
            continue
        if timestamps:
            start = format_timestamp(float(segment.start))
            end = format_timestamp(float(segment.end))
            lines.append(f"[{start} --> {end}] {text}")
        else:
            lines.append(text)

    output_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    print(f"[INFO] 已輸出：{output_path}")


def transcript_path_for(audio_path: Path, output_dir: Path) -> Path:
    """依音檔檔名產生輸出 txt 路徑。"""
    return output_dir / f"{audio_path.stem}.txt"


def main() -> int:
    args = parse_args()
    try:
        audio_files = collect_audio_files(args.audio, args.input_dir)
        output_dir = args.output_dir.expanduser()
        model, actual_device, actual_compute_type = load_model(
            args.model,
            args.device,
            args.compute_type,
        )
        print(
            f"[INFO] 實際使用：device={actual_device}, "
            f"compute_type={actual_compute_type}, files={len(audio_files)}"
        )

        for audio_path in audio_files:
            segments, info = transcribe_audio(
                model,
                audio_path,
                args.language,
                args.vad_filter,
            )
            detected_language = getattr(info, "language", None)
            if detected_language:
                print(f"[INFO] 偵測語言：{detected_language}")
            save_transcript(
                segments,
                transcript_path_for(audio_path, output_dir),
                args.timestamps,
            )
        return 0
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

# Speech-to-Text（語音轉文字）工具

本工具使用 faster-whisper（Whisper 高速推論套件）將音檔轉成文字逐字稿，適用於課程錄音整理、學習筆記、報告講稿、會議紀錄，以及中文與中英混合語音辨識。工具放在獨立路徑 `tools/speech_to_text/`，不依賴 Week1 教材，也不需要修改既有 notes、demo 或 practice。

## 功能說明

- 支援單一音檔轉錄。
- 支援資料夾批次轉錄。
- 支援 `.mp3`、`.wav`、`.m4a`、`.aac`、`.flac`、`.ogg`。
- 預設模型為 `large-v3-turbo`。
- 預設語言為 `zh`，也可用 `--language auto` 讓模型自動偵測。
- 預設啟用 VAD（語音活動偵測），可用 `--no-vad` 關閉。
- 可輸出純文字或逐段時間戳。
- 優先嘗試 CUDA（NVIDIA 平行運算平台）GPU 加速；CUDA 不可用時 fallback（降級執行）到 CPU（中央處理器）。

## 系統需求

Windows：

- Windows 10 或 Windows 11。
- Python 3.10 或以上。
- NVIDIA GPU（NVIDIA 顯示卡）可選。
- CUDA 可選；若無 GPU 或 CUDA 不可用，可使用 CPU 模式。

Linux：

- Ubuntu 22.04 或以上。
- Python 3.10 或以上。
- NVIDIA GPU 可選。
- CUDA 可選；若無 GPU 或 CUDA 不可用，可使用 CPU 模式。

CUDA 相關安裝可能依作業系統、顯卡驅動、CUDA Runtime（CUDA 執行環境）、cuDNN（深度神經網路加速函式庫）與 Python 版本而不同。若第一次建置環境，建議先用 `small` 模型與 CPU 模式確認工具可正常執行。

## 安裝 Python

Windows：

1. 到 Python 官方網站安裝 Python 3.10 或以上版本。
2. 安裝時勾選 `Add Python to PATH`。
3. 安裝後開啟新的終端機，執行 `python --version` 確認版本。

Linux：

```bash
python3 --version
sudo apt update
sudo apt install python3-pip python3-venv
```

## 建立虛擬環境

Windows PowerShell：

```powershell
cd tools/speech_to_text
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

若 PowerShell 無法啟用虛擬環境，可先在同一個 PowerShell 視窗執行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

Windows CMD：

```bat
cd tools\speech_to_text
python -m venv .venv
.venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
```

Linux：

```bash
cd tools/speech_to_text
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 放置音檔

將待轉錄音檔放在：

```text
tools/speech_to_text/audio/
```

輸出逐字稿預設會寫入：

```text
tools/speech_to_text/transcripts/
```

若輸出資料夾不存在，程式會自動建立。

## 單一音檔轉錄

```bash
python transcribe.py --audio audio/test.mp3
```

預設會輸出：

```text
transcripts/test.txt
```

第一次測試建議使用較小模型與 CPU：

```bash
python transcribe.py --audio audio/test.mp3 --model small --device cpu
```

## 批次轉錄整個資料夾

```bash
python transcribe.py --input-dir audio
```

程式會掃描 `audio/` 內所有支援格式音檔，並為每個音檔輸出獨立 `.txt` 逐字稿。

## 指定輸出資料夾、模型、語言、時間戳

指定輸出資料夾：

```bash
python transcribe.py --audio audio/test.mp3 --output-dir transcripts
```

指定模型：

```bash
python transcribe.py --audio audio/test.mp3 --model medium
```

指定語言：

```bash
python transcribe.py --audio audio/test.mp3 --language zh
```

自動偵測語言：

```bash
python transcribe.py --audio audio/test.mp3 --language auto
```

輸出時間戳：

```bash
python transcribe.py --audio audio/test.mp3 --timestamps
```

時間戳輸出格式如下：

```text
[00:00:01.20 --> 00:00:05.80] 這是一段轉錄文字。
[00:00:06.10 --> 00:00:09.40] 這是下一段轉錄文字。
```

未啟用時間戳時，只輸出純文字：

```text
這是一段轉錄文字。
這是下一段轉錄文字。
```

## 命令列參數

| 參數 | 用途 | 範例 |
| --- | --- | --- |
| `--audio` | 指定單一音檔路徑。 | `python transcribe.py --audio audio/test.mp3` |
| `--input-dir` | 指定音檔資料夾，批次處理所有支援格式。 | `python transcribe.py --input-dir audio` |
| `--output-dir` | 指定輸出資料夾，預設 `transcripts`。 | `python transcribe.py --audio audio/test.mp3 --output-dir transcripts` |
| `--model` | 指定 Whisper 模型名稱，預設 `large-v3-turbo`。 | `python transcribe.py --audio audio/test.mp3 --model medium` |
| `--language` | 指定語言，預設 `zh`；`auto` 表示自動偵測。 | `python transcribe.py --audio audio/test.mp3 --language auto` |
| `--timestamps` | 輸出逐段時間戳。 | `python transcribe.py --audio audio/test.mp3 --timestamps` |
| `--device` | 指定 `auto`、`cuda` 或 `cpu`，預設 `auto`。 | `python transcribe.py --audio audio/test.mp3 --device auto` |
| `--compute-type` | 指定 `auto`、`float16`、`int8`、`int8_float16`，預設 `auto`。 | `python transcribe.py --audio audio/test.mp3 --compute-type float16` |
| `--vad` | 啟用 VAD，預設啟用。 | `python transcribe.py --audio audio/test.mp3 --vad` |
| `--no-vad` | 關閉 VAD，避免內容被靜音過濾切掉。 | `python transcribe.py --audio audio/test.mp3 --no-vad` |

## 使用 GPU 與 CPU

- `--device auto`：預設模式。程式會先嘗試 CUDA；若 CUDA 不可用，會改用 CPU。
- `--device cuda`：嘗試使用 CUDA；若初始化失敗，程式會印出可能原因並 fallback 到 CPU。
- `--device cpu`：強制使用 CPU，適合第一次測試或沒有 NVIDIA GPU 的環境。

若使用 CUDA，`--compute-type auto` 會使用 `float16`。若使用 CPU，`--compute-type auto` 會使用 `int8`。

CUDA 初始化失敗時，常見原因包含 NVIDIA driver 尚未安裝或版本不符、CUDA Runtime 缺失、cuDNN 缺失、`faster-whisper` 或 `ctranslate2` 依賴不完整、Python 虛擬環境套件安裝錯誤。

## VAD 說明

VAD（語音活動偵測）可以協助過濾靜音段，預設啟用：

```bash
python transcribe.py --audio audio/test.mp3 --vad
```

若錄音內容被切掉、停頓很長或背景音讓判斷不穩定，可嘗試關閉 VAD：

```bash
python transcribe.py --audio audio/test.mp3 --no-vad
```

## 第一次執行注意事項

- 第一次執行會下載模型，需要網路。
- `large-v3` 與 `large-v3-turbo` 模型較大，下載與初始化時間較長。
- 模型通常會快取在本機，下次執行會較快。
- CPU 模式可作為保底方案，但速度會明顯慢於 GPU。
- 若網路、權限或磁碟空間不足，模型下載可能失敗。

## 模型選擇建議

| 模型 | 特點 | 建議用途 |
| --- | --- | --- |
| `small` | 速度快，準確率普通。 | 快速測試。 |
| `medium` | 速度與準確率平衡。 | 一般中文錄音。 |
| `large-v3` | 準確率高，速度較慢。 | 品質優先。 |
| `large-v3-turbo` | 速度快且準確率佳。 | 推薦預設，GPU 環境可優先使用。 |

## Windows 常見問題

`python` 不是內部或外部命令：

- 重新安裝 Python，確認勾選 `Add Python to PATH`。
- 關閉並重新開啟終端機。

PowerShell 無法啟用虛擬環境：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

CUDA 無法使用：

- 執行 `nvidia-smi` 確認驅動程式是否正常。
- 確認 CUDA Runtime、cuDNN 與 Python 套件版本相容。
- 先用 `--device cpu --model small` 驗證工具本身可執行。

第一次執行很慢：

- 第一次會下載與載入模型，屬於正常現象。

中文標點或專有名詞不準：

- 可嘗試更大的模型，例如 `medium`、`large-v3` 或 `large-v3-turbo`。
- 確認音檔音量、背景噪音與麥克風品質。

## Linux 常見問題

`python` 指令不存在：

```bash
python3 --version
```

若系統只有 `python3`，請使用 `python3 -m venv .venv` 建立環境。

`pip` 不存在：

```bash
sudo apt update
sudo apt install python3-pip python3-venv
```

CUDA 無法使用：

```bash
nvidia-smi
```

若 `nvidia-smi` 無法正常顯示 GPU，請先檢查 NVIDIA 驅動程式與 CUDA 安裝。

## 建議使用流程

1. 第一次測試先使用 `small` 模型與 CPU：

   ```bash
   python transcribe.py --audio audio/test.mp3 --model small --device cpu
   ```

2. 確認可執行後，改用預設模型與自動裝置選擇：

   ```bash
   python transcribe.py --input-dir audio --model large-v3-turbo --language zh
   ```

3. 需要時間戳時加入 `--timestamps`：

   ```bash
   python transcribe.py --input-dir audio --model large-v3-turbo --language zh --timestamps
   ```

## 驗收指令

```bash
python transcribe.py --audio audio/test.mp3
python transcribe.py --input-dir audio
python transcribe.py --audio audio/test.mp3 --model large-v3-turbo
python transcribe.py --audio audio/test.mp3 --device cpu --model medium
python transcribe.py --audio audio/test.mp3 --timestamps
```

有 `audio/test.mp3` 時，應產生：

```text
transcripts/test.txt
```

"""Read-only Qwen2.5-VL adapter that converts one RGB frame into semantic JSON."""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class AdapterConfig:
    model_id: str = "Qwen/Qwen2.5-VL-3B-Instruct"
    revision: str = "main"
    device: str = "auto"
    dtype: str = "auto"
    max_new_tokens: int = 160
    prompt: str = (
        "Return JSON only with keys objects, relations, uncertain. "
        "objects is a list of visible object names; relations is a list of spatial relation strings; "
        "uncertain is a list of unsupported or ambiguous claims. Do not output robot commands."
    )


class RealVLMAdapter:
    """Lazy model wrapper; construction loads the real checkpoint once."""

    def __init__(self, config: AdapterConfig):
        import torch
        from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration

        self.config = config
        self.torch = torch
        dtype = "auto" if config.dtype == "auto" else getattr(torch, config.dtype)
        started = time.perf_counter()
        self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            config.model_id,
            revision=config.revision,
            torch_dtype=dtype,
            device_map=config.device,
        ).eval()
        self.processor = AutoProcessor.from_pretrained(config.model_id, revision=config.revision)
        self.load_seconds = time.perf_counter() - started

    @staticmethod
    def _parse_json(text: str) -> dict[str, Any]:
        candidate = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.IGNORECASE)
        parsed = json.loads(candidate)
        if not isinstance(parsed, dict):
            raise ValueError("VLM response must be a JSON object")
        for key in ("objects", "relations", "uncertain"):
            if not isinstance(parsed.get(key), list):
                raise ValueError(f"VLM response field {key!r} must be a list")
        return {key: parsed[key] for key in ("objects", "relations", "uncertain")}

    def infer(self, rgb_frame: Any) -> tuple[dict[str, Any], dict[str, Any]]:
        from PIL import Image

        image = Image.fromarray(rgb_frame)
        messages = [{"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": self.config.prompt},
        ]}]
        prompt = self.processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.processor(text=[prompt], images=[image], padding=True, return_tensors="pt").to(
            self.model.device
        )
        if self.torch.cuda.is_available():
            self.torch.cuda.reset_peak_memory_stats()
        started = time.perf_counter()
        with self.torch.inference_mode():
            output = self.model.generate(
                **inputs,
                max_new_tokens=self.config.max_new_tokens,
                do_sample=False,
            )
        if self.torch.cuda.is_available():
            self.torch.cuda.synchronize()
        inference_ms = (time.perf_counter() - started) * 1000
        generated = output[:, inputs.input_ids.shape[1] :]
        text = self.processor.batch_decode(
            generated, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )[0]
        semantic = self._parse_json(text)
        evidence = {
            "model_id": self.config.model_id,
            "revision": self.config.revision,
            "device": str(self.model.device),
            "dtype": str(next(self.model.parameters()).dtype),
            "input_shapes": {key: list(value.shape) for key, value in inputs.items() if hasattr(value, "shape")},
            "generated_tokens": int(generated.shape[1]),
            "load_seconds": self.load_seconds,
            "inference_ms": inference_ms,
            "raw_answer": text,
            "peak_vram_mb": (
                self.torch.cuda.max_memory_allocated() / 1024**2
                if self.torch.cuda.is_available()
                else None
            ),
        }
        return semantic, evidence

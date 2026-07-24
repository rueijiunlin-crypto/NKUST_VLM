"""Create actual image/state/language/timestamp tensors and inspect their contract."""
import argparse
import time


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--image", help="Optional local image; otherwise create a synthetic sensor frame.")
    p.add_argument("--text", default="pick up the red block")
    p.add_argument("--device", default="cpu")
    p.add_argument("--model-id", default="google-bert/bert-base-uncased")
    p.add_argument("--revision", default="main")
    args = p.parse_args()
    import torch
    from PIL import Image
    from transformers import AutoTokenizer

    image = Image.open(args.image).convert("RGB") if args.image else Image.new("RGB", (224, 224), "gray")
    image_tensor = torch.asarray(bytearray(image.tobytes()), dtype=torch.uint8).reshape(image.height, image.width, 3)
    image_tensor = image_tensor.permute(2, 0, 1).unsqueeze(0).float().div(255).to(args.device)
    state = torch.tensor([[0.0, 0.1, -0.2, 0.3, 0.0, 0.2, -0.1, 1.0]], device=args.device)
    tokenizer = AutoTokenizer.from_pretrained(args.model_id, revision=args.revision)
    language = tokenizer(args.text, return_tensors="pt").to(args.device)
    timestamps = torch.tensor(
        [[time.time(), time.time(), time.time()]], dtype=torch.float64, device=args.device
    )
    print(f"model_id={args.model_id} revision={args.revision} device={args.device}")
    print(f"image={tuple(image_tensor.shape)} {image_tensor.dtype} {image_tensor.device}")
    print(f"state={tuple(state.shape)} {state.dtype} {state.device}")
    print(
        f"input_ids={tuple(language['input_ids'].shape)} {language['input_ids'].dtype} "
        f"attention_mask={tuple(language['attention_mask'].shape)} device={language['input_ids'].device}"
    )
    print(
        f"timestamps={tuple(timestamps.shape)} {timestamps.dtype} {timestamps.device} "
        f"max_skew_ms={(timestamps.max()-timestamps.min())*1000:.3f}"
    )


if __name__ == "__main__":
    main()

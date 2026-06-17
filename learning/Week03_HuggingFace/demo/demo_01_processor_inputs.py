"""觀察 Hugging Face CLIPProcessor 如何輸出圖文輸入張量。"""

from __future__ import annotations #這行代碼啟用了 Python 的未來功能，允許在類定義中使用類型註解，這對於提高代碼的可讀性和維護性非常有幫助。

import argparse #argparse 模組用於解析命令列參數，讓使用者可以在執行腳本時指定圖片路徑等參數。
from pathlib import Path #pathlib 模組提供了面向對象的文件系統路徑操作，Path 類可以方便地處理文件和目錄路徑。


MODEL_NAME = "openai/clip-vit-base-patch32"
DEFAULT_LABELS = [ #這些是我們提供給 CLIPProcessor 的候選標籤（prompts），用來描述圖像的內容。CLIP 模型會將這些文本標籤與圖像進行比較，以判斷圖像最有可能對應哪個標籤。
    "a photo of a cat",
    "a photo of a dog",
    "a photo of a pink sofa",
    "a photo of a robot",
]


def parse_args() -> argparse.Namespace: #parse_args 函式用來解析命令列參數，預期接收一個 --image 參數，指定本地圖片的路徑。
    parser = argparse.ArgumentParser(description=__doc__) #創建一個 ArgumentParser 對象，description 參數使用了 __doc__，這會將模塊的文檔字符串作為說明文字顯示在命令列幫助信息中。
    parser.add_argument("--image", type=Path, required=True, help="本地圖片路徑。") #添加一個必需的命令列參數 --image，類型為 Path，這樣使用者在執行腳本時必須提供圖片的路徑。help 參數提供了該參數的說明文字。
    return parser.parse_args()


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPProcessor
    except ImportError as error:
        print(f"缺少套件：{error.name}")
        print("請安裝依賴：python -m pip install -r demo/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"圖片路徑不存在：{args.image}")
        print("若 Week02 範例圖片不存在，請改用自己的本地圖片路徑。")
        return 1

    image = Image.open(args.image).convert("RGB")

    print("正在載入 processor（前處理器）。第一次執行可能會下載檔案。")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME) #CLIPProcessor 是 Hugging Face Transformers 庫中專門為 CLIP 模型設計的前處理器，能夠同時處理圖像和文本輸入。
    inputs = processor(
        text=DEFAULT_LABELS, #text 參數接受一個字符串列表，這些字符串是模型用來比較圖像的候選標籤（prompts）。在這裡，我們提供了四個描述不同物體的標籤。
        images=image,        #images 參數接受一個 PIL 圖像對象，這是我們從指定路徑載入的圖片。CLIPProcessor 會自動對圖像進行必要的預處理，如調整大小和正規化。
        return_tensors="pt", #return_tensors 參數指定輸出格式為 PyTorch 張量（"pt"）。這意味著 processor 會將處理後的圖像和文本數據轉換為 PyTorch 張量，方便直接輸入到 CLIPModel 中進行推理。
        padding=True,        #padding 參數設置為 True，表示對文本輸入進行填充，使得所有文本序列的長度相同。這對於批量處理非常重要，因為模型需要固定長度的輸入。
    )

    print(f"模型：{MODEL_NAME}")
    print(f"圖片路徑：{args.image}")
    print("候選 labels（標籤）：")
    for label in DEFAULT_LABELS: #迭代輸出我們提供給 processor 的候選標籤，這些標籤是模型用來比較圖像的文本描述。
        print(f"- {label}")      #這裡的輸出只是顯示我們提供給 processor 的原始文本標籤，實際送入模型的是經過 tokenizer 處理後的 input_ids 和 attention_mask 張量。

    print("\nProcessor 輸出 keys（欄位）與 shape（形狀）：")
    for key, value in inputs.items():
        print(f"- {key}: shape={tuple(value.shape)}, dtype={value.dtype}")

    print("\n解讀：")
    print("- input_ids / attention_mask 來自文字 prompts（提示詞）。")
    print("- pixel_values 來自圖片 resize（調整尺寸）與 normalization（正規化）後的結果。")
    print("- 這些 tensor（張量）才是送進 CLIPModel 的實際輸入。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Speech-to-Text 使用範例

第一次測試建議先放一個短音檔到 `audio/test.mp3`，再執行：

```bash
python transcribe.py --audio audio/test.mp3 --model small --device cpu
```

確認 CPU 模式可執行後，可改用預設模型與自動裝置選擇：

```bash
python transcribe.py --input-dir audio --model large-v3-turbo --language zh
```

若需要保留每段時間戳：

```bash
python transcribe.py --input-dir audio --model large-v3-turbo --language zh --timestamps
```

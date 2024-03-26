## usage

PDF画像化 + OCR による PDFテキスト化コードサンプル。
処理したいPDFファイルを `./data/sample.py` に配置する。

```sh
brew install poppler tesseract tesseract-lang
poetry install
cd pdf2text
poetry run python main.py
```

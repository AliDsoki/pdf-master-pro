name: Build PDF Master Pro (onedir)

on:
  push:
    branches: [ main ]
  workflow_dispatch: {}

jobs:
  build-windows:
    runs-on: windows-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Build with PyInstaller (onedir)
        run: pyinstaller PDF_Master_Pro.spec --noconfirm --clean

      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: PDFMasterPro-windows
          path: dist/PDFMasterPro/

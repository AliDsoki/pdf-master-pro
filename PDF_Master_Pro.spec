# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['PDF_Master_Pro_v10_23.py'],          # 1) اسم الملف الجديد
    pathex=[],
    binaries=[],
    datas=[('extract_pdf.ico', '.')],
    hiddenimports=['google.genai', 'pymupdf', 'fitz'],   # 2) pymupdf بدل pypdf
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pikepdf', 'pypdf', 'PyPDF2', 'pdfrw'],    # 3) استبعاد المحركات الاحتياطية
    noarchive=False,
)

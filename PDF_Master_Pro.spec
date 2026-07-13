# -*- mode: python ; coding: utf-8 -*-
# بناء PDF Master Pro في وضع onedir (مجلد وليس ملف واحد)

block_cipher = None

a = Analysis(
    ['PDF_Master_Pro_v3_5.py'],
    pathex=[],
    binaries=[],
    datas=[
        # ضع هنا أي أصول تريد تضمينها داخل حزمة التطبيق (اختياري):
        # ('extract_pdf.ico', '.'),
        # ('splash.png', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,  # مهم: يبقي الملفات خارج EXE => onedir
    name='PDFMasterPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # واجهة رسومية بلا نافذة كونسول
    icon='extract_pdf.ico', # احذف هذا السطر إن لم يوجد ملف أيقونة
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PDFMasterPro',    # الناتج: dist/PDFMasterPro/ (مجلد كامل)
)

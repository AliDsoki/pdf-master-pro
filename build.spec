# -*- mode: python ; coding: utf-8 -*-
# ملف بناء PyInstaller لبرنامج PDF Master Pro
# وضع onedir: مجلد فيه exe + مكتبات بدون ضغط (أسرع تشغيل، حجم أكبر)
# بدون نافذة كونسول (windowed)

import os

block_cipher = None

# لو موجود ملف أيقونة .ico في نفس المجلد هيتضاف تلقائياً، لو مش موجود هيبني من غير أيقونة
icon_file = "extract_pdf.ico" if os.path.exists("extract_pdf.ico") else None

datas = []
if os.path.exists("extract_pdf.ico"):
    datas.append(("extract_pdf.ico", "."))

a = Analysis(
    ["PDF_Master_Pro_v29_1.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        "google.genai",
        "google.genai.types",
        "google.genai.errors",
        "pypdf",
    ],
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
    exclude_binaries=True,   # ✅ onedir: البيانات/المكتبات بتتحط في مجلد منفصل، مش جوه الـ exe
    name="PDF_Master_Pro",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_file,
)

# ✅ onedir: تجميع الـ exe مع كل المكتبات والبيانات في مجلد واحد dist/PDF_Master_Pro/
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="PDF_Master_Pro",
)

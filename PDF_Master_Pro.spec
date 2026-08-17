# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['PDF_Master_Pro_v9_7.py'],
    pathex=[],
    binaries=[],
    # ✅ إصلاح: أضف ملف الأيقونة هنا حتى يُنسخ بجانب الـ exe الناتج —
    # الكود يبحث عنه في نفس مجلد البرنامج باسم extract_pdf.ico (أو
    # pdf_master.ico / pdf_master_icon.png) عبر resolve_app_icon_path().
    # ضع ملف الأيقونة بجوار هذا الـ .spec قبل البناء بنفس الاسم.
    datas=[('extract_pdf.ico', '.')],
    hiddenimports=['google.genai', 'pypdf'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PDFMasterPro',
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
    # ✅ إصلاح: هذا هو ما يُظهر الأيقونة على ملف الـ exe نفسه في
    # مستكشف الملفات — كان مفقوداً تماماً من قبل.
    icon='extract_pdf.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PDFMasterPro',
)

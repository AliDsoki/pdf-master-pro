# PDF Master Pro

معالج ملفات PDF و TXT احترافي بالعربية — استخراج، مقارنة، وإعادة معالجة باستخدام Gemini API.

## البنية

```
.
├── PDF_Master_Pro_v29_1.py     # الكود الرئيسي
├── build.spec                  # إعدادات PyInstaller لبناء exe واحد بدون console
├── requirements.txt            # المكتبات المطلوبة
├── .github/workflows/build.yml # بناء تلقائي على GitHub Actions
└── extract_pdf.ico             # (اختياري) أيقونة البرنامج — أضِفها هنا لو موجودة عندك
```

## طريقة الرفع على GitHub (أول مرة)

من مجلد المشروع على جهازك:

```bash
git init
git add .
git commit -m "PDF Master Pro v29.1"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git push -u origin main
```

استبدل `USERNAME/REPO_NAME` باسم حسابك واسم الريبو اللي هتعمله على GitHub.

## البناء التلقائي

بمجرد الـ push، هيشتغل GitHub Actions تلقائياً ويبني نسخة exe لويندوز.
تقدر تتابع التقدم من تبويب **Actions** في صفحة الريبو.

بعد ما البناء يخلص:
- هتلاقي الملف الناتج تحت **Actions → آخر تشغيل → Artifacts → PDF_Master_Pro-windows-exe**

### لعمل إصدار (Release) رسمي بالـ exe مرفق تلقائياً

اعمل تاج بصيغة `v` ثم رقم النسخة وارفعه:

```bash
git tag v29.1
git push origin v29.1
```

هيتعمل Release تلقائي على GitHub وهيترفع عليه ملف `PDF_Master_Pro.exe` مباشرة، وأي حد يقدر يحمّله من صفحة Releases من غير ما يدخل على Actions.

## البناء يدوياً بدون GitHub (على جهازك)

```bash
pip install -r requirements.txt
pip install pyinstaller
pyinstaller build.spec
```

الناتج هيكون في `dist/PDF_Master_Pro.exe`

## ملاحظات مهمة

- مفاتيح Gemini API (`keys_state.json`, `keys_global_state.json`) **متضافة تلقائياً في `.gitignore`** ومش هترفع على GitHub — ده مقصود عشان أمان مفاتيحك.
- لو عندك ملف أيقونة `extract_pdf.ico`، ضيفه في نفس مجلد الكود قبل الرفع وهيتضمّن تلقائياً في الـ exe.
- البناء بيتم على `windows-latest` عشان الـ exe يبقى متوافق مع ويندوز.

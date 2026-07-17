@echo off
chcp 65001 >nul
pip install -r requirements.txt pyinstaller
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
pyinstaller pdf_master_pro.spec
pause

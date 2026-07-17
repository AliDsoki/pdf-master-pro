#!/usr/bin/env bash
set -e
pip install -r requirements.txt pyinstaller
rm -rf build dist
pyinstaller pdf_master_pro.spec

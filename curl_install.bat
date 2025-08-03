@echo off
echo 🤖 Brampton AI - One-Click Installation
echo ========================================

REM Download and run the installation script
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/arindam0025/Brampton-/main/install_one_liner.py' -OutFile 'temp_install.py'"
python temp_install.py
del temp_install.py 
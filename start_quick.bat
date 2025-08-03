@echo off
echo 🏦 Brampton Finance AI - Quick Start
echo =====================================

echo 📦 Installing backend dependencies...
cd backend
pip install -r requirements.txt

echo 🚀 Starting backend server...
start "Brampton Backend" cmd /k "uvicorn main:app --reload --host 0.0.0.0 --port 8000"

echo ⏳ Waiting for backend to start...
timeout /t 5 /nobreak > nul

echo 🌐 Opening frontend...
cd ..\frontend
start "" "index.html"

echo ✅ Brampton Finance AI is now running!
echo    Backend: http://localhost:8000
echo    Frontend: Opened in your default browser
echo.
echo Press any key to exit...
pause > nul

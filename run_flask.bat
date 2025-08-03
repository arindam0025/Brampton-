@echo off
echo Starting Brampton Finance AI Flask App...
echo.

REM Set the API key environment variable
set OPENROUTER_API_KEY=your-api-key-here

REM Install requirements if needed
pip install flask gunicorn requests

REM Start the Flask app
echo Flask app starting at http://localhost:5000
echo.
python flask_app.py

pause

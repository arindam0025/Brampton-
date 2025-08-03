@echo off
echo Starting Brampton Finance AI Flask App...
echo.

REM Set the API key environment variable
set OPENROUTER_API_KEY=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

REM Install requirements if needed
pip install flask gunicorn requests

REM Start the Flask app
echo Flask app starting at http://localhost:5000
echo.
python flask_app.py

pause

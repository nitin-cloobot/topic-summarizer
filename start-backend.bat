@echo off
echo ========================================
echo Starting Backend Server
echo ========================================
echo.

cd backend

echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Starting Flask server...
echo Backend will be available at http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python run.py


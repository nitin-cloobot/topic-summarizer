@echo off
echo ========================================
echo Backend Setup Script
echo ========================================
echo.

cd backend

echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo Backend setup complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create a .env file in the backend directory
echo 2. Add your Gemini API key to the .env file
echo 3. Run start-backend.bat to start the server
echo.
echo Press any key to exit...
pause > nul


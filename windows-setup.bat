@echo off
REM Change to the script directory
cd /d "C:\Users\Corso Robotica\Documents\Network-Analysis-tool"

echo Do not close...

REM Check if the scheduled task exists
schtasks /Query /TN "PingTool-v9" >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Creating scheduled task "PingTool-v9"...
    schtasks /Create /TN "PingTool-v9" /TR "\"C:\Users\Corso Robotica\Documents\Network-Analysis-tool\windows-setup.bat\"" /SC HOURLY /F
)

REM Activate the venv and run the script with logging
call "C:\Users\Corso Robotica\Documents\Network-Analysis-tool\venv\Scripts\activate.bat"
python logic.py >nul 2>> "C:\Users\Corso Robotica\Documents\Network-Analysis-tool\ping_errors.log"
call "C:\Users\Corso Robotica\Documents\Network-Analysis-tool\venv\Scripts\deactivate.bat"

echo Done!

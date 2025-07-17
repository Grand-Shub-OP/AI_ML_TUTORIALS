@echo off
cd /d "%~dp0"
git status > git_status_log.txt
git add .
git commit -m "Auto commit on %date% %time%" >> git_status_log.txt 2>&1
git push >> git_status_log.txt 2>&1
pause

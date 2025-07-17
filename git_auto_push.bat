@echo off
cd /d "%~dp0"
git add .
git commit -m "Auto commit on %date% %time%"
git pull --rebase
git push
pause

@echo off
echo ===================================
echo  Adding all files to Git...
echo ===================================
git add .

echo.
echo ===================================
echo  Committing the changes...
echo ===================================
git commit -m "Auto-commit on %date% %time%"

echo.
echo ===================================
echo  Pushing to GitHub...
echo ===================================
git push

echo.
echo ===================================
echo  All done!
echo ===================================
pause

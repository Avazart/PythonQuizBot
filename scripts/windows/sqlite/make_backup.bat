@echo off
cd ..
call set_env.bat

echo.
echo NEW_BACKUP_PATH: "%NEW_BACKUP_PATH%"
echo. 

@echo on
"%SQLITE_TOOL_PATH%"  "%SQLITE_DATABASE%" .dump > %NEW_BACKUP_PATH%


pause


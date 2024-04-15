@echo off
cd ..
call set_env.bat

echo.
echo LAST_BACKUP_PATH: "%LAST_BACKUP_PATH%"
echo.

@echo on
"%SQLITE_TOOL_PATH%" "%SQLITE_DATABASE%" < "scripts/drop_tables_sqlite.sql"
"%SQLITE_TOOL_PATH%" "%SQLITE_DATABASE%" < "%LAST_BACKUP_PATH%"

@echo off
echo.
echo LAST_BACKUP_PATH: "%LAST_BACKUP_PATH%"
echo.

pause
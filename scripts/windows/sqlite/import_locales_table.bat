cd ..
call set_env.bat

@echo on
"%SQLITE_TOOL_PATH%" "%SQLITE_DATABASE%" < scripts\locales_table_sqlite.sql
pause
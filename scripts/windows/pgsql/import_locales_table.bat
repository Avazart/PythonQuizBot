@echo off
cd ..
call set_env.bat

echo on
"%PSQL_PATH%" -f "scripts\locales_table_pgsql.sql"
pause
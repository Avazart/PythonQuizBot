cd ..
call set_env.bat

"%PSQL_PATH%" -f "scripts\drop_schema.sql"

pause
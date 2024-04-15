PRAGMA foreign_keys=off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS locales;
DROP TABLE IF EXISTS alembic_version;

COMMIT;
PRAGMA foreign_keys=on;



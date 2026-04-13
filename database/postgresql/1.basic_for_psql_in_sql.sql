CREATE DATABASE mydb;

CREATE USER siddharth WITH PASSWORD 'sid@1906';

ALTER ROLE siddharth SET client_encoding TO 'utf8';
ALTER ROLE siddharth SET default_transaction_isolation TO 'read committed';
ALTER ROLE siddharth SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE mydb TO siddharth;
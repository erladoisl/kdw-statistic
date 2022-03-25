import psycopg2
import dbapi.config as c

conn_string = f"host={c.PGHOST} " +\
    "port=5432 " +\
              f"dbname={c.PGDATABASE} " +\
              f"user={c.PGUSER} " +\
              f"password={c.PGPASSWORD}"
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

import psycopg2
import dbapi.config as c
import pandas as pd

# Set up a connection to the postgres server.
conn_string = f"host={c.PGHOST} " +\
    "port=5432 " +\
              f"dbname={c.PGDATABASE} " +\
              f"user={c.PGUSER} " +\
              f"password={c.PGPASSWORD}"
conn = psycopg2.connect(conn_string)
print("Connected!")

# Create a cursor object
cursor = conn.cursor()


def table_names():
    sql_query = " SELECT *                                    " +\
         "          FROM pg_catalog.pg_tables                 " +\
        f"          WHERE schemaname != 'pg_catalog' AND      " +\
        f"                schemaname != 'information_schema'; "
    return pd.read_sql(sql_query, conn)
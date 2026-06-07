from io import StringIO
import csv

def psql_insert_copy(table, conn, keys, data_iter):
    dbapi_conn = conn.connection

    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        csv.writer(s_buf).writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join(f'"{k}"' for k in keys)
        table_name = (
            f"{table.schema}.{table.name}"
            if table.schema
            else table.name
        )

        cur.copy_expert(
            sql=f"COPY {table_name} ({columns}) FROM STDIN WITH CSV",
            file=s_buf
        )

import mariadb
import psycopg2
import sqlite3
import sys


def connect_to_databases(db_url, db_user, db_password):
    db_url_params = db_url.split(':')
    db_type = db_url_params[1]
    db_host = db_url_params[2].replace('//','')
    db_port = int(db_url_params[3].split('/')[0])
    db_database = db_url_params[3].split('/')[1]
    connection = None
    connect_params ={
        'user': db_user,
        'password': db_password,
        'host': db_host,
        'port': db_port,
        'database': db_database
    }
    if db_type == 'mariadb' or db_type == 'mysql':
        try:
            connection = mariadb.connect(
                **connect_params
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    elif db_type == 'postgresql':
        try:
            connection = psycopg2.connect(
                **connect_params
            )
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL Platform: {e}")
            sys.exit(1)
    elif db_type == 'sqllite3':
        try:
            connection = sqlite3.connect(
                # **connect_params
            )
        except sqlite3.Error as e:
            print(f"Error connecting to sqlite3 Platform: {e}")
            sys.exit(1)
    connection.autocommit = False
    return connection


def execute_sql(connection, sql, get_result, *execute_many_data):
    cur = connection.cursor()
    if len(execute_many_data) > 0:
        cur.executemany(sql, execute_many_data[0])
    else:
        cur.execute(sql)
    if not sql.lower().strip().startswith('select'):
        connection.commit()
    row_values = []
    if get_result and type(get_result).__name__ == 'bool':
        results = cur.fetchall()
        col_names = []
        for col in cur.description:
            col_names.append(col[0])
        row_values.append(col_names)
        for row in results:
            values = []
            for value in row:
                values.append(value)
            row_values.append(values)
        for rw in row_values:
            print(rw)
    cur.close()
    # connection.close()
    if sql.lower().__contains__('select'):
        return row_values


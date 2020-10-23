import mariadb
import psycopg2
import sys


def connect_to_databases(db_type, db_host, db_port, db_database, db_user, db_password):
    conn = None
    connect_params ={
        'user': db_user,
        'password': db_password,
        'host': db_host,
        'port': db_port,
        'database': db_database
    }
    if db_type == 'mariadb':
        try:
            conn = mariadb.connect(
                **connect_params
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    elif db_type == 'postgresql':
        try:
            conn = psycopg2.connect(
                **connect_params
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    conn.autocommit = False
    return conn


def execute_query(connection, sql):
    cur = connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    col_names = []
    row_values = []
    for col in cur.description:
        col_names.append(col[0])
    row_values.append(col_names)
    for row in results:
        values = []
        for value in row:
            values.append(value)
        row_values.append(values)
    cur.close()
    connection.close()
    for rw in row_values:
        print(rw)

# maria_connection = connect_to_databases('mariadb', '172.21.100.91', 3306, 'mysql', 'debianmysql', 'debianmysqlpasswd')
# execute_query(maria_connection, 'select * from user')

postgresql_connection = connect_to_databases('postgresql', '172.21.100.91', 5432, 'pgtest', 'debianpgsql',
                                             'debianpgsqlpasswd')
execute_query(postgresql_connection, 'select * from student')





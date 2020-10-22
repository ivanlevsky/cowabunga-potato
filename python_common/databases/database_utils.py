import mariadb
import sys


def connect_to_databases(db_type, db_host, db_port, db_database, db_user, db_password):
    conn = None
    if db_type == 'mariadb':
        try:
            conn = mariadb.connect(
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
                database=db_database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    # conn.autocommit = False
    return conn


def excute_query(connection, sql):
    cur = connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    connection.close()


maria_connection = connect_to_databases('mariadb', '172.21.100.124', 3306, 'mysql', 'debianmysql', 'debianmysqlpasswd')
excute_query(maria_connection, 'select * from user')






from datasets.database_utils import connect_to_databases, execute_sql
from python_common.global_param import mariadb_url,mariadb_user,mariadb_password
from python_common.global_param import pgsql_url,pgsql_user,pgsql_password


sql = 'select * from student'
maria_connection = connect_to_databases(mariadb_url,mariadb_user, mariadb_password)
execute_sql(maria_connection, sql, True)

postgresql_connection = connect_to_databases(pgsql_url, pgsql_user, pgsql_password)
execute_sql(postgresql_connection,  sql, True)


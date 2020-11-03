from datasets.database_utils import connect_to_databases, execute_sql
from datasets.datasets_utils import read_excel, write_excel
from python_common.global_param import mariadb_url, mariadb_user, mariadb_password, excel_datasets
from python_common.global_param import pgsql_url,pgsql_user,pgsql_password

# create table
create_table_sql = '''
        CREATE TABLE movie
        (
            id INT PRIMARY KEY  NOT NULL,
            name        VARCHAR(100) NOT NULL,
            chnname     VARCHAR(50),
            main_cast        VARCHAR(50),
            year         VARCHAR(10) NOT NULL,
            region      VARCHAR(20) NOT NULL,
            type        VARCHAR(20),
            viewed     VARCHAR(5) NOT NULL,
            want_to_review   VARCHAR(5) NOT NULL
        );
      '''
maria_connection = connect_to_databases(mariadb_url,mariadb_user, mariadb_password)
execute_sql(maria_connection, create_table_sql, False)
maria_connection.close()
postgresql_connection = connect_to_databases(pgsql_url, pgsql_user, pgsql_password)
execute_sql(postgresql_connection,  create_table_sql, False)
postgresql_connection.close()


# read excel sheet datasets then insert into database table
insert_many_sql = '''
        INSERT INTO movie (id, name, chnname, main_cast, year, region, type, viewed, want_to_review)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
      '''
data = read_excel(excel_datasets, 'movie', True, dtype=str)
maria_connection = connect_to_databases(mariadb_url,mariadb_user, mariadb_password)
execute_sql(maria_connection, insert_many_sql, False, data)
maria_connection.close()
postgresql_connection = connect_to_databases(pgsql_url, pgsql_user, pgsql_password)
execute_sql(postgresql_connection,  insert_many_sql, False, data)
postgresql_connection.close()

# connection to mysql, postgresql and write query sql results to excel sheet
query_sql = 'select * from movie'
maria_connection = connect_to_databases(mariadb_url,mariadb_user, mariadb_password)
mariadb_row_values = execute_sql(maria_connection, query_sql, True)
maria_connection.close()
postgresql_connection = connect_to_databases(pgsql_url, pgsql_user, pgsql_password)
pgsql_row_values = execute_sql(postgresql_connection,  query_sql, True)
postgresql_connection.close()
write_excel(excel_datasets,'movie_maria', mariadb_row_values,False)
write_excel(excel_datasets,'movie_pg', pgsql_row_values,True)



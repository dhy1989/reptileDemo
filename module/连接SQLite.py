import sqlite3
import pandas.io.sql as sql

connect = sqlite3.connect(':memory:')


def create_table(con):
    query = '''
    create table if not exists test(
        id int (11) primary key,
        'name' varchar (10),
        age int (2)
    )
    '''
    con.execute(query)
    con.commit()


def insert_data(con):
    query = '''
    insert into test values(1,'张三',15),(2,'李四',16)
    '''
    con.execute(query)
    con.commit()


# 创建表
create_table(connect)

# 添加数据
insert_data(connect)
query = sql.read_sql_query('select * from test', connect)
print(query)
connect.close()

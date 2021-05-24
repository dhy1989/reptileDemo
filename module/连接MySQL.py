import pymysql
import pandas.io.sql as sql

con = pymysql.connect(host='192.168.23.200',
                      user='dhy',
                      password='123456',
                      db='test',
                      charset='utf8',
                      )
data = sql.read_sql('select * from bank limit 10', con)

print(data.to_string())

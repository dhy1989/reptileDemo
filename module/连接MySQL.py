import pymysql
import pandas.io.sql as sql

con = pymysql.connect(host='rm-k1hdeu6e84gx7zq2q.mysql.rds.aliyuncs.com',
                      user='portal_test',
                      password='Hmd(0Hd12fzx',
                      db='crm_portal_test',
                      charset='utf8',
                      )
data = sql.read_sql('select * from bank limit 10', con)

print(data.to_string())

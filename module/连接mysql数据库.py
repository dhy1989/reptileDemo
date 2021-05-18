import pymysql

db = pymysql.connect(host='rm-k1hdeu6e84gx7zq2q.mysql.rds.aliyuncs.com', user='portal_test', password='Hmd(0Hd12fzx',
                     port=3306, db='crm_portal_test')
cursor = db.cursor()
execute = cursor.execute('select* from')
data = cursor.fetchone()

print("Database version : %s " % data)
db.close()

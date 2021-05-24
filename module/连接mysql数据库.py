import pymysql

db = pymysql.connect(host='192.168.23.200', user='dhy', password='123456',
                     port=3306, db='test')
cursor = db.cursor()
execute = cursor.execute('select* from')
data = cursor.fetchone()

print("Database version : %s " % data)
db.close()

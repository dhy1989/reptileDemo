import xlrd

data = xlrd.open_workbook('C:/Users/ThinkPad/Desktop/员工表(更新).xlsx')
sheet = data.sheets()[0]
nrows = sheet.nrows


def _aaa(value):
    s = str(value)
    splits = s.split(".")[0]
    return splits

for i in range(nrows):
    values = sheet.row_values(i)
    # print(values)
    # type(values)
    'username', 'qq', 'mobile'
    if i != 0:
        sql = 'update employee set '
        if values[1] == '' and values[2] != '':
            sql += 'mobile=' + "'" + _aaa(values[2]) + "'"
        if values[1] != '' and values[2] == '':
            sql += 'qq=' + "'" + _aaa(values[1]) + "'"
        if values[1] != '' and values[2] != '':
            sql += 'qq=' + "'" + _aaa(values[1]) + "',"
            sql += 'mobile=' + "'" + _aaa(values[2]) + "'"
        sql += 'where username=' + "'" + values[0] + "'"
        print(sql+";")

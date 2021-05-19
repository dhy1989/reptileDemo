import csv

string = '';
with open('C:/Users/ThinkPad/Desktop/tb_bdmap_rail.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)
    for i in range(len(result)):
        if i != 0:
            temp = result[i][1] + '-'
            if temp not in string:
                string += temp
            string += "[" + result[i][3] + "," + result[i][4] + "]"
        if i != len(result) - 1 and i != 0:
            string += ","
with open('C:/Users/ThinkPad/Desktop/经纬度.txt', 'w',encoding='UTF-8') as f:
    f.write(string)

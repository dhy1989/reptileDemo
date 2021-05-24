import json

import pandas as pd

print(pd.__version__)

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}
frame = pd.DataFrame(mydataset)
print(frame)
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
name_series = pd.Series(names)
print(name_series)
print(names[0])
# sites里边的key 1,2,3作为索引
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
sites_series = pd.Series(sites, name="RUNOOB-Series-TEST")
print(sites_series)
# 如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可
sites_series2 = pd.Series(sites, index=[1, 3], name="RUNOOB-Series-TEST2")
print(sites_series2)

# DataFrame
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=float)
print(df)

# 使用ndarrays创建
data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}
df = pd.DataFrame(data)
print(df)
# 使用字典创建,没有对应的部分数据为 NaN
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
# loc根据索引返回指定行的数据
print(df.loc[0])
print(df.loc[[0, 1]])  # 返回多行


# pandas处理csv文件
def csv_to_data():
    csv = pd.read_csv('nba.csv')
    print(csv.to_string())  # to_string() 用于返回 DataFrame 类型的数据
    print(csv)  # 不使用to_string(),则输出结果为数据的前面 5 行和末尾 5 行，直接部分以 ... 代替


# 将数据转为csv文件
def data_to_csv():
    nme = ["Google", "Runoob", "Taobao", "Wiki"]
    st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
    ag = [90, 40, 80, 98]
    dict = {'name': nme, 'site': st, 'age': ag}
    df = pd.DataFrame(dict)
    print(df)
    df.to_csv('site.csv')


# head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行
def head_data():
    csv = pd.read_csv('nba.csv')
    print(csv.head(10).to_string())


# tail(n)读取尾部, 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN
def tail_data():
    csv = pd.read_csv('nba.csv')
    print(csv.tail(10).to_string())


# info()返回表格的一些基本信息
def info_data():
    csv = pd.read_csv('nba.csv')
    print(csv.info())


# pandas读取json文件数据
def json_to_data():
    json_data = pd.read_json('site.json')
    print(json_data.to_string())


def json_data():
    data = [
        {
            "id": "A001",
            "name": "菜鸟教程",
            "url": "www.runoob.com",
            "likes": 61
        },
        {
            "id": "A002",
            "name": "Google",
            "url": "www.google.com",
            "likes": 124
        },
        {
            "id": "A003",
            "name": "淘宝",
            "url": "www.taobao.com",
            "likes": 45
        }
    ]
    df = pd.DataFrame(data)
    print(df)


# 直接读取json的url
def json_url():
    URL = 'https://static.runoob.com/download/sites.json'
    df = pd.read_json(URL)
    print(df)


# 读取内嵌的json数据,使用到 json_normalize() 方法将内嵌的数据完整的解析出来
def inner_json():
    read_json = pd.read_json('nested_list.json')
    print(read_json.to_string())
    # 使用 Python JSON 模块载入数据
    with open('nested_list.json', 'r') as f:
        data1 = json.loads(f.read())
        # 展平数据
        df_nested_list = pd.json_normalize(data1, record_path=['students'])
        print(df_nested_list)


def job_info():
    company = ['百度', '谷歌', '360', '阿里巴巴']
    job = ['开发工程师', '数据分析师', '产品经理', 'UI设计']
    jobinfo = pd.DataFrame([company, job])
    jobinfo = jobinfo.T  # 将列转置成行
    jobinfo.columns = ['公司', '职位']  # 设置列的标题
    print(jobinfo)
    print(jobinfo['职位'])  # 获取列
    print(jobinfo.loc[0])  # 获取行
    jobinfo.index = ['a', 'b', 'c', 'd']  # 设置索引
    print(jobinfo)
    jobinfo = jobinfo.reset_index()  # 重置索引,之前的索引会变成列
    # jobinfo = jobinfo.reset_index(drop=True) # 直接删除索引,使用默认索引
    print(jobinfo)
    print(jobinfo)


job_info()

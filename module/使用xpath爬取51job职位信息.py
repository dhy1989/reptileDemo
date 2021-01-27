import requests
from lxml import etree
import json
from pandas import DataFrame

new_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,java,2,1.html'
response = requests.get(url, headers=new_headers)
response.encoding = 'gbk'
# 利用etree初始化xpath对象
root = etree.HTML(response.text)
scripts = root.xpath('//script[@type="text/javascript"]/text()')
print(type(scripts))
strip = scripts[0].strip()
str_json = strip[27:len(strip)]
loads = json.loads(str_json)
print(type(loads))
result_ = loads['engine_search_result']
print(result_[0])
position = []
salary = []
work_place = []
company = []
for i in result_:
    position.append(i['job_name'])
    salary.append(i['providesalary_text'])
    company.append(i['company_name'])
    work_place.append(i['workarea_text'])

jobInfo = DataFrame([position, company, work_place, salary]).T
jobInfo.columns = ['职位', '公司', '工作地点', '工资']
print(jobInfo)
jobInfo.to_csv('51job.csv')
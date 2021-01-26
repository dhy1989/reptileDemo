import requests
from lxml import etree
import json
new_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url='https://search.51job.com/list/010000,000000,0000,00,9,99,java,2,1.html'
response = requests.get(url, headers=new_headers)
response.encoding='gbk'
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

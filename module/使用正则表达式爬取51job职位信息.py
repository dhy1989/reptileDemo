import requests
import re
import json
new_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,java,2,1.html'
response = requests.get(url, headers=new_headers)
response.encoding = 'gbk'
print(response.text)
import requests
import re

url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=1.his.0.0&wq=&pvid=1980c9f523b54e3d9ca6f3489e78afbb';
new_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}
request = requests.get(url=url, headers=new_headers)
request.encoding = 'UTF-8'
path1 = '<img width="220" height="220" data-img="1" .*="//(.*?)" />'
findall = re.findall(path1, request.text)


def down_pic(pic_url,i):
    response = requests.get('https://' + pic_url)
    with open('F:\\python\\reptileDemo\\module\\pic\\'+i+'.jpg', 'wb') as fd:
        fd.write(response.content)

for i in range(len(findall)):
    down_pic(findall[i],str(i))
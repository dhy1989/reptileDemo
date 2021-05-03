import requests
new_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url = 'https://docs.apipost.cn/view/3488477031d91e86#2381319'
response = requests.get(url, headers=new_headers)
response.encoding = 'UTF-8'
text = response.text
print(text)

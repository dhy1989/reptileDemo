import requests

# get请求
requests_get = requests.get('http://poetry.apiopen.top/getTime')
print(requests_get.status_code)
json = requests_get.json()
print(requests_get.headers)
print(json)
print(type(requests_get))

# post请求
post = requests.post('https://api.apiopen.top/getWangYiNews', data={'page': 1, 'count': 5})
post_json = post.json()
print(post_json)
print(type(post_json))
print(post_json['code'])

# 传递url参数
payload = {'page': 1, 'count': 5}
get = requests.get('https://api.apiopen.top/getWangYiNews', payload)
print(get.json())

# 请求网页内容
r = requests.get('http://www.baidu.com')
print(r.text)
# 解决乱码问题
r.encoding = 'UTF-8'
print(r.text)

# 请求图片内容
response = requests.get('https://www.youmeitu.com/Upload/20200103/1578045960301804.jpg')
print(response.content)
with open('美女.jpg', 'wb') as fd:
    for chunk in response.iter_content(2):
        fd.write(chunk)
# 定制请求头
headers = {'user-agent': 'my-app/0.0.1'}
res = requests.get('http://poetry.apiopen.top/getTime', headers)
print(res.status_code)

# post上传一个文件
url = 'http://httpbin.org/post'
files = {'file': open('美女.jpg', 'rb')}
r = requests.post(url, files=files)
print(r.text)
from urllib import request, parse
import json

# res = request.urlopen('http://poetry.apiopen.top/getTime')
# print(type(res))
# decode = res.read().decode('UTF-8')
# print(decode)

# Get请求
# with request.urlopen('http://poetry.apiopen.top/getTime') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# 伪装成手机
# req = request.Request('http://www.baidu.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# POST请求
# param = {'page': 1, 'count': 5}
# data = parse.urlencode(param)
# print(data)
# req = request.Request('https://api.apiopen.top/getWangYiNews')
# with request.urlopen(req, data=data.encode('UTF-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     decode = f.read().decode('utf-8')
#     loads = json.loads(decode)
#     print(loads)
#     print(type(decode))

# 下载图片
url = "https://www.youmeitu.com/Upload/20200103/1578045960301804.jpg";
with request.urlopen(url) as f:
    read = f.read()
    print(read)
    file = open('美女.jpg', 'wb')
    file.write(read)
    file.close()

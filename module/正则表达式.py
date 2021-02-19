import re

# ------正则表达式匹配
# 字符串
test = 'ABC-001'
# 正则表达式
reg = r'ABC\-001'
if re.match(reg, test):
    print('ok')
else:
    print('failed')

# 正则表达式切割
re_split = re.split(r'\s+', 'a b   c')
print(re_split)

print(re.match('www', 'www.runoob.com'))  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

reg = r'^(?![0-9]+$)(?![a-zA-Z]+$)(?![_]+$)[0-9A-Za-z_]{6,20}$'
test = 'dinghy123'
if re.match(reg, test):
    print('ok')
else:
    print('failed')

reg = r'^[a-z0-9_-]{3,16}$'
if re.match(reg, '111'):
    print('ok')
else:
    print('failed')

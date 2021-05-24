import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.dtype)

# 多维度数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# 类型字段名可以用于存取实际的 age 列
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])
# 下面的示例定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象
student = np.dtype([('name', 'O'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)

# ndarray.ndim 用于返回数组的维数，等于秩
a = np.arange(24)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim)

# ndarray.shape返回一个元组，这个元组的长度就是维度的数目
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)

# ndarry.zeros ones 使用0或者1填充
zeros = np.zeros((3, 6))
print(zeros)

# 花式索引
e = np.arange(32)
e1 = np.reshape(e, (8, 4))
print(e1)
print(e1[0])  # 常规索引
print(e1[[2, 3, 1]])  # 花式索引传入一个数组,获取对应行的索引
print(e1[[0, 1, 2], [3, 2, 1]])  # 选取多行多列交叉处的元素
#  获取矩形区域2种方式
print(e1[[1, 5, 7, 2]][:, [0, 3, 2, 1]])
print(e1[np.ix_([1, 5, 7, 2], [0, 3, 2, 1])])  # np.ix_获取矩形区域

# 通用函数(ufunc)
f = np.arange(9)
print(np.sqrt(f))  # 开根号
j = np.arange(5)
k = np.array([4, 5, 6, 7, 2])  # 每个位上的数值进行相加
print(np.add(j, k))
print(np.maximum(j, k))  # 每个位上的数值进行比较,取最大值

print(f.max())  # 最大值
print(f.min())  # 最小值
f.sort()  # 排序
print(f)
print(f.mean())  # 均值

# 多维数组操作
arr1 = np.random.randn(5, 3)
arr1.sort()  # 对每行进行排序
print(arr1)
arr1.sort(axis=0)  # 对每列进行排序
print(arr1)

# np.linspace 等分,2和5参数表示对应端点个数
linspace = np.linspace(0, 10, 2)
print(linspace)
linspace = np.linspace(0, 10, 5)
print(linspace)
print(np.linspace(0, 10, 11))  # 0-10之间11个数

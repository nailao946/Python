# for...in ... 的简单运用
print('= = = =for...in... = = = = =')
print('range(0,5)')
for z in range(0, 5):
    print(z)

print('range(0,6)')
for y in range(0, 6):
    print(y)

print('range(1,5)')
for x in range(1, 5):
    print(x)

# 字典
print('= = = = 字典 = = = =')
dict = {'name': 'ylx', 'age': '18', '修改字典-当前0': '修改字典当前为0'}
print(dict['name'])
print(dict['age'])

print(dict['修改字典-当前0'])
dict['修改字典-当前0'] = '修改字典当前为1'  # 修改字典
print(dict['修改字典-当前0'])

print(len(dict))  # 记录字典元素个数
print(type(dict))  # 返回变量类型 dict为变量

print('name' in dict)  # 判断'name'是不是在字典，在的话返回true

# 元组
print('= = = = 元组 = = = = =')
a = ('Googel', '余隆鑫', '没jj')
#       0        1      2    元组的序列
print(a[0])
num1 = (1, 2)
num2 = ('nam', 'e')
num3 = num1 + num2  # 元组加
print(num3)

num4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print('最大值:', max(num4))  # 求最大值
# print(sum(num1+num2))
# copy = ('Hi')*4 # 复制
# print(copy)

# 转码
print('= = = 转码 = = =')
s = '哈哈'
a = s.encode('utf-8')
print(s.encode('utf-8'))  # 转码
print(a.decode('utf-8'))  # 解码

# 列表
list = ['松鼠党', '国王', '猎魔人', '狩魔猎人', '巫师', '狂猎']
list.append('hehe')  # 添加数据
print(list)

list.insert(2, 'haha')  # 指定位置添加
print(list)
# list.reverse()  # 反转
# print(list)

list.remove('狂猎')  # 移除
print(list)

list.pop(0)
print(list)  # 移除指定位置的
# ctrl+左键查看更多用法 左边'准心'定位函数列表（准心右边的齿轮状设置要设置'显示成员'）

# 拷贝
print(' = = = = 拷贝 = = = =')
a = [1, 2, 3, 4, 5, 6]
print(id(a))
b = a
print(id(b))
b = a.copy()
print(id(b))

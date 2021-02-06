age = [11, 22, 12, 32, 12, 31, 44]
x = filter(lambda a: a > 18, age)
# 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
print(x)  # 输出的是一个对象 <filter object at 0x000001D030501A60>
print(list(x))

age = [11, 22, 12, 32, 12, 31, 44]
x = map(lambda a: a + 2, age)
print(x)  # 输出的是一个对象 <filter object at 0x000001D030501A60>
print(list(x))  # 全部加2

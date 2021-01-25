apend = lambda a, b: a + b
# lambda为匿名函数
# 用来表达一个简单的函数,函数调用的次数很少，基本.上就是调用一次
# 调用匿名函数两种方式:
# 1.给它定义一个名字(很少这样使用)
# 2.把这个函数当做参数传给另-个函数使用(使用场景比较多)
print(apend(1, 2))


# 可在出现一个函数调用不同两种函数情况使用
def calc(a, b, f):
    return f(a, b)


# f则作为选择用哪一个函数进行运算
def adition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


print(calc(2, 1, lambda a, b: a * b))  # 也可以直接用匿名函数
print(calc(2, 1, adition))
print(calc(2, 1, subtraction))

# 函数内部的变量和函数外部的变量是相互独立的互不影响
# 函数内部为局部变量，函数外部为全局变量
# 有返回值的函数
def add(a, b):
    c = a + b
    # return c
    return a + b  # return 返回一个函数的执行后的结果


# 没有返回值的函数
x = print('这是一个内置函数print')
print(x)  # 如果一个函数没有返回值，那么返回为None

c = '证明：函数内和函数外变量是独立的'
print(c, add(10, 1))

# 要想要在函数里面使用全局变量 需要用  global 变量
def get():
    global c
    c = '成功修改全局变量'
# 查看全局变量和查看局部变量
# 使用globals（） 和 locals（）
# print('全局变量',globals())

get()
print(c)
#   函数的文档说明
def getmax(num1:int, num2:int):  # num1：建议的类型，鼠标常放在调用的函数上有意见
    '''
    这个函数用来取两个值中的较大的一个
    :param num1: 数值1
    :param num2: 数值2
    :return: 返回出来的最大值
    '''
    if num1 < num2:
        print(num2)
    else:
        print(num1)

# help(getmax)  # 用来调用函数帮助
getmax(125, 128937)



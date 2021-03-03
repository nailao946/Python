def div(a, b):
    return a / b


try:
    x = div(5, 2)
except Exception as e:
    #  其他的报错提示都指向 Exception 所以可以代表大部分报错
    print('程序出错')
else:
    print('计算结果是：', x)



age = input('输入年龄：')

if age != float(age):
    print('输入数字')
#     如果输入 aaa 的话 ValueError: invalid literal for int() with base 10: 'aaa'
#     会出现一个叫做ValueError的报错
#     如果想要掠过ValueError，让ValueError不影响程序而且可以达到判断效果就要用下面的方法
else:
    if age > 18:
        print('>18')
    else:
        print('<18')


try:
    age = float(age)
except ValueError as e:
    print('输入数字！')
#     如果出现了报错就等于输入的值是存在问题，直接输出 print的
else:
    if age > 18:
        print('>18')
    else:
        print('<18')
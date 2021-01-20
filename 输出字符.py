# %s 表示的字符是占位符
# %d 表示的是整数占位符
# %nd 打印时，以n位显示，如果不够，在前面用空格补齐
# %f 表示是浮点数占位符
# %.nf 表示浮点数后面位数
# %x 用十六进制输出
name = '赫赫'
age = 11
tall = 1.75
print('名字:%2s 年龄:%d 身高:%.2f' % (name, age, tall))
print('%.2f' % 3.1415926)

# format()运用
# {} {} {} {}
#  0 1  2   3
x = '年龄：{}  名字{}'.format(18, 'syx')
print(x)
print('a{}b{}c{}d{}'.format(0, 1, 2, 3, 4))
# {数字}{变量}可以混合使用
# {}{数字}不可以混合使用
x = ["zhangshan", 18, "hunan"]
print("{},{},{}".format(*x))

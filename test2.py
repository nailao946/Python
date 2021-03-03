# 求最大数
def getmax(*args):
    a = 0
    for arg in args:
        a = a + arg
    print(a)


# 摇骰子
import random


def touzi():
    a = [1, 2, 3, 4, 5, 6]
    print(random.choice(a))

# csv文件的读写
# import csv
#
# a = open('xx.csv', 'w', encoding='utf-8')
# # w = csv.writer(a)
# # w.writerow(['name', 'age', 'id'])


# 写到内存
# from io import StringIO
#
# xd = StringIO()
# xd.write('你好')
# print(xd.getvalue())
import sys
a = sys.stdin

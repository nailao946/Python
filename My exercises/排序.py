# 20.12.28 获得成就：独立视频写出来的比大小，写了半个小时
num = [1, 7, 3, 8, 8, 9, 2]
n = 0
count = 0
while n < len(num):
    a = 0
    a += n
    while a < len(num) - 1:
        count += 1
        if num[n] < num[a + 1]:
            num[n], num[a + 1] = num[a + 1], num[n]
        a += 1
    n += 1
print(num)
print(count)
# 更加简单的方法 自带的函数
# 递增排序 sort
# num.sort()
# # num.reverse()
# print(num)
# 递减可以直接反转或者 num.sort(reverse = True)

# 内置函数sorted用法
x = sorted(num, reverse=True)
print(x)

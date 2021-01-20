import random
#
# a = [(x, y) for x in range(1, 3) for y in range(1, 3)]
# b = [[], [], []]
# for i in a:
#     c = random.choice(b)
#     c.append(i)
# print(b)
# for d, b in enumerate(a):
#     print('第%d个房间 有%d个老师分别是：' % (d, len(b)))
#     for i in b:
#         print(b, end='')
a = int(input('输入学生数量：'))
x1 = int(input('输入组数：'))
y1 = int(input('输入列数：'))
group = [(x, y) for x in range(1, x1 + 1) for y in range(1, y1 + 1)]
students = [student for student in range(1, a + 1)]
print(group)
for i in students:
    c = random.choice(group)
    print(i, c)

import copy

# 浅拷贝只复制指向某个对象的指针，而不复制对象本身，新旧对象还是共享同一块内存。
# 但深拷贝会另外创造一个一模一样的对象，新对象跟原对象不共享内存，修改新对象不会改到原对象。
# 深拷贝要用copy模块

# 浅拷贝：
a = [1, 2, ['a', 'b', 'c'], 4, 5, 6, 7]
# b = a.copy()  # 拷贝出去后的内容一致，内存地址不是同一个
# print(a, id(a))
# print(b, id(b))
# print('')
#
# a[0] = 9  # 修改时候也不会变化
# print(a, id(a))
# print(b, id(b))
# print('')
# a[2][0] = 's'  # 但是修改列表里面的列表则会一同复制过去
#                  因为列表里面的列表是指向同一个内存地址
# print(id(a[2])) ## 使用这个就可以看到列表里面的列表的内存地址了
#
# print(a, id(a))
# print(b, id(b))
# 深拷贝
b = copy.deepcopy(a)
a[2][0] = 's'  # 深拷贝则是完全复制，内存独立
print(id(a))
print(id(a[2]))
print(b, id(b))

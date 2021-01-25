a = [2, 3, 6, 1, 7, 9, 0]
c = a.copy()  # 复制一个不同内存的
a.sort()  # 用sort进行排序
print(a)  # 可以看到输出的结果是把原来的列表给重新排序了

sorted(c)  # 用sorted进行排序
print(c,id(c))  # 可以看到原来的列表是不变的
print(sorted(c),id(sorted(c)))  # 直接输出sorted的排序可以看出，sorted是生成了一个新的排序好了的列表
                                # 内存也不一样
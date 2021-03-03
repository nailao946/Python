student = [{'name': 'xindao', 'age': 17},
           {'name': 'hutao', 'age': 16},
           {'name': 'ziyou', 'age': 18},
           {'name': 'xiandao', 'age': 30},
           ]


def x(sort):
    return sort['age']

student.sort(key=x)

# 如果给定了键函数，则对每个列表项应用一次，并根据它们的函数值升序或降序排序。
print(student)
#
#
#
# calc = [{'num': 3},
#         {'num': 2},
#         {'num': 4},
#         {'num': 5}
#         ]
#
#
# def adition(x):
#     print(1 + x['num'])
#
#
# calc.sort(key=adition)

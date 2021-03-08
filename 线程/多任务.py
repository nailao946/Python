import threading


def a(x):
    for i in range(10):
        print('任务1')


def b():
    for i in range(10):
        print('任务2')


# 创建线程
thread_a = threading.Thread(target=a, args=(1,))  # 给函数传递参数
thread_b = threading.Thread(target=b)
# 启动线程
thread_a.start()
thread_b.start()

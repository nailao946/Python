import threading

tick = 100

lock = threading.Lock()
def selltick():
    global tick
    while True:
        lock.acquire()
        if tick > 0:
            lock.release()
            tick -= 1
            print('线程{}出售了一张,剩下{}张.'.format(threading.current_thread().name, tick))
        else:
            lock.release()
            print('卖完了!')
            break


s1 = threading.Thread(target=selltick, name='1')
s2 = threading.Thread(target=selltick, name='2')
s1.start()
s2.start()

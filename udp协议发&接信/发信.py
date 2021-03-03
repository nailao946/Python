import socket

'''
1.AF_INET:表示这个socket是用来网络连接
2.SOCK_DGRAM：表示链接是一个udp链接
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('ylx sb'.encode('utf8'), ('10.20.228.93', 9090))
s.close()

# s.connect('127.0.0.1',9090)

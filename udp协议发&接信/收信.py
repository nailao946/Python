import socket

'''
1.AF_INET:表示这个socket是用来网络连接
2.SOCK_DGRAM：表示链接是一个udp链接
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 9090))
c = s.recvfrom(1024)
print(c)
s.close()

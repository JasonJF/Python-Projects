import socket

UDP_IP = "10.10.100.58"
UDP_PORT = 5005
MESSAGE = "Hello, World"
print "UDP target IP :", UDP_IP
print "UDP target PORT :", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))

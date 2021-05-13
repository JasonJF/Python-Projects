import socket

UDP_IP = "10.10.100.20"
UDP_PORT = 12289
MESSAGE = "Hello, World"
print "UDP target IP :", UDP_IP
print "UDP target PORT :", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message:", data)

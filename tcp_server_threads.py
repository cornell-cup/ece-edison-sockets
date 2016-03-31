''' TCP Server with threads '''
import sys
import socket
from thread import * 
# import mraa

def client_thread(sock, address):
    sock.sendall("You are now connected to the server\n")
    while True:
        # receiving data from client
        data = sock.recv(1024)
        msg = 'You sent: ' + data
        if not data:
            break
        sock.sendall(msg)
    print "Client (%s,%s) is offline" % address
    sock.close()

if __name__ == "__main__":
    HOST = ''   
    PORT = 6789 

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    print "Server is listening"

    while True:
        sock, addr = server.accept()
        print "Client (%s, %s) connected" % addr
        start_new_thread(client_thread, (sock,addr))

    server.close()
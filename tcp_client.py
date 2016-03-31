import socket
import select
import string
import sys

def prompt(myName):
    # myName is a string which will be an alias for the client (used just for display)
    sys.stdout.write('<' + myName + '> ')
    sys.stdout.flush()


# main function
if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print 'Usage: python tcp_client.py HOSTNAME PORT'
        sys.exit()

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    RECV_BUFFER = 4096

    c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_sock.settimeout(2)

    # connect to remote host
    try: 
        c_sock.connect((HOST, PORT))
    except :
        print 'Unable to connect'
        sys.exit()

    print 'Connected to host ' + str(HOST) + 'Start sending messages'
    prompt('ME')

    while True:
        socket_list = [sys.stdin, c_sock]

        # Get the sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            # incoming message from remote server 
            if sock == c_sock:
                data = sock.recv(RECV_BUFFER)
                if not data:
                    print '\nDisconnected from TCP server'
                    sys.exit()
                else:
                    # print data
                    sys.stdout.write(data)
                    prompt('ME')

            #user entered a message 
            else:
                msg = sys.stdin.readline()
                c_sock.send(msg)
                prompt('ME')

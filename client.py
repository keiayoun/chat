import sys
import socket
import select

def main():
    if len(sys.argv) != 2:
        print("correct usage: script, name")
        exit()

    host = "127.0.0.1"
    port = 8080
    name = str(sys.argv[1])
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))

    while 1:
        sockets_list = [sys.stdin, server]
        read_sockets,_, _ = select.select(sockets_list,[],[])

        for socks in read_sockets:
            if socks == server:
                msg = socks.recv(2048)
                print(msg.decode())
            else:
                msg = sys.stdin.readline()
                server.send(msg.encode())

main()

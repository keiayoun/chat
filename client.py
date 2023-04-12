import sys
import socket
import select
import os

def main():
    if len(sys.argv) != 1:
        print("correct usage: script")
        exit()

    host = "127.0.0.1"
    port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))

    print("What is your name?")
    name = sys.stdin.readline()
    server.send(name.encode())
    os.system('clear')

    while 1:
        sockets_list = [sys.stdin, server]
        read_sockets,_, _ = select.select(sockets_list,[],[])
        try:
            for socks in read_sockets:
                if socks == server:
                    msg = socks.recv(2048)
                    print(msg.decode())
                else:
                    msg = sys.stdin.readline()
                    server.send(msg.encode())
        except:
            os.system('clear')
            print("<chat closed>")
            break

main()

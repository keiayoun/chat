import sys
import socket
from chat.client import Client
from thread import *

def main():
    # program start
    print(sys.version)
    print("program start")

    # initialize socket and port
    host = "127.0.0.1"
    port = "8080"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    # while loop
        # listen for new clients
        # new clients will then go to worker threads
    while 1:
        s.listen()
        conn, addr = s.accept()
        worker_thread(conn, addr)

def worker_thread(conn, addr):
    while 1:
        # wait for msg
        msg = "hello"
        # if msg is exit, close this connection and exit
        if msg == "hello":
            break
        # send msg
        print(msg)

main()

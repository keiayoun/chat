import sys
import socket
import threading

https://prod.liveshare.vsengsaas.visualstudio.com/join?26ABF7BBC7248B8173C525910C98D20ACDDB

def main():
    # program start
    print(sys.version)
    print("program start")

    # initialize socket and port
    print("\n================================")
    print("binding host and port to server socket...")
    host = "127.0.0.1"
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))

    # while loop
        # listen for new clients
        # new clients will then go to worker threads
    print("\n================================")
    print("server will now accept clients...")
    while 1:
        sock.listen()
        connection, address = sock.accept()
        print("found new client!!")
        client = threading.Thread(target=worker_thread, args=(connection, address))
        client.start()

    sock.close()

def worker_thread(conn, addr):
    print("starting " + addr[0] + " client!")
    while 1:
        # wait for msg
        msg = conn.recv(2048)

        # prints client's msg to server side
        print("<" + addr[0] + ">" + msg)

        # if msg is exit, close this connection and exit
        if msg == "exit":
            break

        # send msg to client
        conn.send(msg)

    # prints to server and client that user has left
    print("<" + addr[0] + " has left>")
    conn.send("<" + addr[0] + " has left>")
    conn.close()

main()

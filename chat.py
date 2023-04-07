import sys
import socket
import threading

threads = []

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
        threads.append(connection)
        client = threading.Thread(target=worker_thread, args=(connection, address))
        client.start()

    sock.close()

def worker_thread(conn, addr):
    print("starting " + addr[0] + " client!")
    while 1:
        # wait for msg
        msg = conn.recv(2048)
        msg = msg.decode()

        # prints client's msg to server side
        msg_self = "<you>" + msg
        msg_other = "<" + addr[0] + ">" + msg
        print(msg)

        # if msg is exit, close this connection and exit
        if msg == "exit":
            break

        # send msg to client
        broadcast_msg(msg_self, msg_other, conn)

    # prints to server and client that user has left
    msg_other = "<" + addr[0] + " has left>"
    msg_self = "<You have left>"
    print(msg_other)
    broadcast_msg(msg_self, msg_other, conn)
    threads.remove(conn)
    conn.close()


def broadcast_msg(msg_self, msg_other, conn):
    msg_self = msg_self.encode()
    msg_other = msg_other.encode()
    for client in threads:
        if client != conn:
            client.send(msg_other)
        else:
            client.send(msg_self)

main()

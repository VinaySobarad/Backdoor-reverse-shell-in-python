import sys
import socket

SERVER_IP=""
PORT= 1234

s= socket.socket()
s.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR)
s.bind((SERVER_IP, PORT))

s.listen(1)

while True:
    print(f"[+] listening {SERVER_IP}:{PORT}")

    client= s.accept()
    print(f"[+] Client connected {client[1]}")

    client[0].send("someone connected".encode())

    while True:
        cmd= input("$$")
        client[0].send(cmd.encode())

        if cmd.lower() in ["quit", "exit", "q", "x"]:
            break

        result= client[0].recv(1024).decode()
        print(result)

    client[0].close

    cmd=input("Wait for the client y/n") or 'y'
    if cmd.lower in ["n", "no"]:
        break 

s.close()

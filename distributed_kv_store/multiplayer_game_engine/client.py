import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))


def receive():
    while True:
        try:
            data = client.recv(1024).decode()
            print("Game State:", data)
        except:
            break


threading.Thread(target=receive).start()

while True:
    move = input("Move (+1 forward / -1 back): ")
    client.send(move.encode())

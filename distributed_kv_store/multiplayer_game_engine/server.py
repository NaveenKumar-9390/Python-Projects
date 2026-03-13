import socket
import threading

clients = []
positions = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5555))
server.listen()

print("Game server started...")


def broadcast(message):
    for client in clients:
        client.send(message.encode())


def handle_client(conn, addr):
    print("Connected:", addr)
    clients.append(conn)
    positions[addr] = 0

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            move = int(data)
            positions[addr] += move
            state = str(positions)
            broadcast(state)

        except:
            break

    clients.remove(conn)
    conn.close()


while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

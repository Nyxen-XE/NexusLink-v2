import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
users = {}

print("===============================")
print("|     NEXUSLINK v2 ACTIVE     |")
print("|      Nyxen-XE Protocol      |")
print("|   Multi-Client Chat System  |")
print("===============================")
def displayOnlineUsers():
    for user in users.keys():
        return user + "\n"


def broadcast(message, sender_socket=None):
    for user, user_socket in users.items():
        try:
            if user_socket != sender_socket:
                user_socket.send(message.encode())
        except:
            pass

def handler_client(client_socket, address):
    try:
        username = client_socket.recv(1024).decode()
        users[username] = client_socket

        print(f"[+] {username} joined from {address[0]}")
        broadcast(f"🟢 {username} has joined the NexusLink ⚡", client_socket)

        while True:
            message = client_socket.recv(1024).decode()
            if message.strip():
                print(f"{username}: {message}")
                broadcast(f"{username} ⚡: {message}", client_socket)
            else:
                break

    except:
        pass
    finally:
        if username in users:
            del users[username]
        client_socket.close()
        broadcast(f"🔴 {username} has left the NexusLink.")
        print(f"[-] {username} disconnected.")

def create_server(ip, port):
    server.bind((ip, port))
    server.listen()
    print(f"\n\t\t🛰️ NexusLink Server Online on {ip}:{port}\n")
    while True:
        client_socket, address = server.accept()
        print(f"[Connection] New client connected from {address}")
        threading.Thread(target=handler_client, args=(client_socket, address), daemon=True).start()

create_server('0.0.0.0', 12345)

import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive_msg():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\n" + message)
        except:
            print("Connection lost.")
            break

def send_msg():
    while True:
        try:
            message = input()
            if message.strip():
                client.send(message.encode())
          
        except:
            break

def start_client(ip, port):
    try:
        client.connect((ip, port))
        print("✅ Connected to NexusLink Server")
        
        while True:
            username = input("Enter your username: ")
            if username.strip():
                client.send(username.encode())
                break
            else:
                continue

        # 🔥 Start message receive/send threads AFTER username is sent
        threading.Thread(target=receive_msg, daemon=True).start()
        send_msg()

    except Exception as e:
        print("Connection failed:", e)

start_client('127.0.0.1', 12345)

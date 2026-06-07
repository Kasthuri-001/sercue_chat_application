import socket
from cryptography.fernet import Fernet

# Load key
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5555))

message = input("You: ")

encrypted_message = cipher.encrypt(message.encode())

client.send(encrypted_message)

# Receive reply
encrypted_reply = client.recv(1024)

reply = cipher.decrypt(encrypted_reply).decode()

print("Server:", reply)

client.close()
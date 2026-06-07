import socket
from cryptography.fernet import Fernet

# Load key
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5555))
server.listen(1)

print("Server is waiting for connection...")

client, address = server.accept()

print("Connected to:", address)

# Receive encrypted message
encrypted_message = client.recv(1024)

decrypted_message = cipher.decrypt(encrypted_message).decode()

print("Client:", decrypted_message)

# Send reply
reply = input("You: ")

encrypted_reply = cipher.encrypt(reply.encode())

client.send(encrypted_reply)

client.close()
server.close()
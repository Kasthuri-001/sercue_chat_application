from cryptography.fernet import Fernet

# Load key from file
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

message = "Secure Message"

encrypted = cipher.encrypt(message.encode())

decrypted = cipher.decrypt(encrypted).decode()

print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
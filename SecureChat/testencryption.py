from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()

# Create cipher object
cipher = Fernet(key)

# Original message
message = "Hello Secure Chat!"

# Encrypt message
encrypted = cipher.encrypt(message.encode())

# Decrypt message
decrypted = cipher.decrypt(encrypted).decode()

print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
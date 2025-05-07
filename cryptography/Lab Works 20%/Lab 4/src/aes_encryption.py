from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Function to pad the message to be compatible with AES block size
def pad_message(message):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    return padded_data

# Function to unpad the message after decryption
def unpad_message(padded_message):
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_message) + unpadder.finalize()
    return data.decode()

# Secret key (must be either 16, 24, or 32 bytes long for AES)
key = os.urandom(32)  # AES-256 key (32 bytes)

# Initialization Vector (IV) - must be 16 bytes for AES
iv = os.urandom(16)

# Sample message
message = "Cryptography Lab by <Your Name, Student ID>!"

# Padding the message
padded_message = pad_message(message)

# Encrypt the message
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_message) + encryptor.finalize()

print(f"Original Message: {message}")
print(f"Ciphertext (hex): {ciphertext.hex()}")

# Decrypt the message
decryptor = cipher.decryptor()
decrypted_padded_message = decryptor.update(ciphertext) + decryptor.finalize()

# Unpad the decrypted message
decrypted_message = unpad_message(decrypted_padded_message)

print(f"Decrypted Message: {decrypted_message}")

from Crypto.Cipher import AES
import os
from hashlib import sha256

KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[:16]  # Fix slicing here

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        ciphertext = f.read()
    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted)
    new_path = filepath.replace(".enc", ".dec")
    with open(new_path, "wb") as f:
        f.write(plaintext)
    print(f"Decrypted {filepath} to {new_path}")

if __name__ == "__main__":
    folder = r"C:\Users\serim\Downloads\simulated_ransomware (1)\locked_files"
    for filename in os.listdir(folder):
        if filename.endswith(".enc"):
            full_path = os.path.join(folder, filename)
            decrypt_file(full_path)

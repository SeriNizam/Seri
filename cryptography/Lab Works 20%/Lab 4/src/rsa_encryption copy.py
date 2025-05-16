# rsa_encryption.py

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

def load_public_key(filename):
    """ Load a public key from PEM file """
    with open(filename, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    return public_key

def load_private_key(filename):
    """ Load a private key from PEM file """
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)
    return private_key

def encrypt_message(plaintext, public_key):
    """ Encrypt plaintext using RSA public key + OAEP padding """
    ciphertext = public_key.encrypt(
        plaintext.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Return Base64 encoded string
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_message(ciphertext_b64, private_key):
    """ Decrypt Base64 encoded ciphertext using RSA private key """
    ciphertext = base64.b64decode(ciphertext_b64)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode('utf-8')

def main():
    print("=== RSA Encryption/Decryption Demo ===")
    print("Choose an option:")
    print("1. Encrypt a message (for your friend)")
    print("2. Decrypt a message (received from friend)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        # ENCRYPT
        plaintext = input("\nEnter plaintext message to encrypt: ").strip()
        pub_key_file = input("Enter filename of receiver's PUBLIC key (e.g., Labu_public_key.pem): ").strip()

        try:
            public_key = load_public_key(pub_key_file)
            encrypted_b64 = encrypt_message(plaintext, public_key)
            print("\n🔐 Encrypted message (Base64 encoded):\n")
            print(encrypted_b64)

        except Exception as e:
            print(f"\n❌ Error: {e}")

    elif choice == '2':
        # DECRYPT
        ciphertext_b64 = input("\nEnter Base64 encoded ciphertext to decrypt: ").strip()
        priv_key_file = input("Enter filename of YOUR PRIVATE key (e.g., Labi_private_key.pem): ").strip()

        try:
            private_key = load_private_key(priv_key_file)
            decrypted = decrypt_message(ciphertext_b64, private_key)
            print("\n✅ Decrypted message:\n")
            print(decrypted)

        except Exception as e:
            print(f"\n❌ Error: {e}")

    else:
        print("\n⚠️ Invalid choice. Please run again and enter 1 or 2.")

if __name__ == "__main__":
    main()

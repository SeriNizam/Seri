import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def sign_message(private_key, message):
    # Sign the message using the private key
    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        # Verify the signature using the public key
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True  # Signature is valid
    except Exception:
        return False  # Signature is invalid

def load_key_from_file(key_file, key_type='private'):
    with open(key_file, 'rb') as f:
        if key_type == 'private':
            return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
        elif key_type == 'public':
            return serialization.load_pem_public_key(f.read(), backend=default_backend())

def save_message_and_signature(message, signature):
    # Save the message to a file
    with open('original_message.txt', 'w') as f:
        f.write(message)
    
    # Save the signature to a file
    with open('message_signature.sig', 'wb') as f:
        f.write(signature)

def load_message_and_signature():
    # Load the message and signature from files
    with open('original_message.txt', 'r') as f:
        message = f.read()

    with open('message_signature.sig', 'rb') as f:
        signature = f.read()

    return message, signature

def main():
    print("=== Digital Signature Demo ===")
    choice = input("Choose an option:\n1. Sign a message\n2. Verify a message\nEnter 1 or 2: ")
    
    if choice == '1':
        # Labi signs the message
        private_key_file = input("Enter your private key file (e.g., Labi_private_key.pem): ")
        private_key = load_key_from_file(private_key_file, key_type='private')

        message = input("Enter the message you want to sign: ")
        
        # Sign the message
        signature = sign_message(private_key, message)

        # Save the message and signature to files
        save_message_and_signature(message, signature)
        print(f"Message signed successfully. The signature and message are saved.")

    elif choice == '2':
        # Labu verifies the signature
        public_key_file = input("Enter the sender's public key file (e.g., Labi_public_key.pem): ")
        public_key = load_key_from_file(public_key_file, key_type='public')

        # Load the message and signature from the files
        message, signature = load_message_and_signature()

        # Verify the signature
        if verify_signature(public_key, message, signature):
            print("Verification successful: The signature is valid!")
        else:
            print("Verification failed: The signature is invalid!")
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    main()

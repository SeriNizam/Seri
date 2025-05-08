___
# Assalamualaikum and Hi everyone 👋🏻
___________________________________________________________________________

So we have come to the last lab work of this subject. This lab work is quite similar to the previous lab work just this time we are using mr snake🐍

Give a round of applause to Mr. Snake, our trusted analyst, as we dive into the world of encryption with Python. Bismillah let's start

>**p/s🤫: get your friend to make this activity more engaging** ❣️

## Requirements 💻🖥️
|Tools | description|
|------|------------|
|VS code| place to do the coding |
|python | script language|

>🚨 python is not installed by default in vscode. So ensure you download the extension first before start the coding process

________________________________


## Task 1️⃣: Symmetric Encryption (AES)🔑
---
1. We are importing required library for this task.
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
```
 ---
2. Now, we are doing the padding, the first fucntion will add padding to encrypted message while the second function is reverse. Unpad will be used during the decryption process. Padding is an important process to ensure out data fit the block size so it will not produce an error.
```python
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
```
> The size of a block is 128 bit = 16 byte
---
3. Here, we are creating a random 32 byte key and 16 byte IV. Since we are using CBC mode, it is encourage to create an IV so it can prevent pattern leakage. This is one of CBC feature.
```python
# Secret key (must be either 16, 24, or 32 bytes long for AES)
key = os.urandom(32)  # AES-256 key (32 bytes)

# Initialization Vector (IV) - must be 16 bytes for AES
iv = os.urandom(16)
```
---
4.  Next, we are going to write or assigned a message that need to be encrypted. Then, we are going to call the use the `pad_message` function and stored it in padded_message.

```python
# Sample message
message = "Cryptography Lab by Seri Binti Mohd Nizam, NWS23010057!"

# Padding the message
padded_message = pad_message(message)
```
---
5.  Now it's time to encrypt the message. So what happen here is we are going to use the AES algorithm on CBC (Block cipher) mode. Then, it will be encrypted by the `.encryptor()` function. .update will encrypt the padded message while `.finalize()` function will ensure the encryption process is completed handles final padding. Finally, we print both the original message (plaintext) and the encrypted one (ciphertext) in hex value.
   
```python
# Encrypt the message
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_message) + encryptor.finalize()

print(f"Original Message: {message}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
```
___
6.  After encrypting, we will decrypt. This code works exactly like encryption just now but this time we are going to use .decryptor() function and unpadded the message to remove the padding and recover get the clean plaintext
   
```python 
# Decrypt the message
decryptor = cipher.decryptor()
decrypted_padded_message = decryptor.update(ciphertext) + decryptor.finalize()

# Unpad the decrypted message
decrypted_message = unpad_message(decrypted_padded_message)

print(f"Decrypted Message: {decrypted_message}")
```
### Output
![alt text](</cryptography/Lab Works 20%25/Lab 4/evidence/aes_encryption_output.png/AES decrypt.png>)

---
## Task 2️⃣: Aymmetric Encryption (RSA)🔑🗝️
_____
## Extra step 👩🏻‍💻
We are going to make a script that will generate both public and private key. But remember this step is optional but advise if you want view the process more clear

```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_keys(name):

    # generate RSA private key
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048,)

    #serialize private key to PEM format
    private_pem =private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # generate public key
    public_key= private_key.public_key()

    #serialize public key to PEM format
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format= serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save the keys to file
    with open (f"{name}_private_key.pem","wb") as private_file:
        private_file.write(private_pem)

    with open (f"{name}_public_key.pem","wb") as public_file:
        public_file.write(public_pem)

    print (f"{name} keys generated are saved!")

#generat keys for Labu and Labi
generate_rsa_keys("Labu")
generate_rsa_keys("Labi")
```
---
1. First of all, import required required library. RSA is the algorithm used for asymmetric encryption, padding serve the same purpose as we mentioned in previous task. Serialization is needed to store and load the key in readable form so that we can just simply upload it. Lastly, we import base64 so that we can encode the ciphertext or keys into base64 format for safe storage of transmission.
```python
# rsa_encryption.py

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64
```
 ---
   2. Next, we are going to create a function to open and load our keys from a file. Once we do this, we can start using it in our code since it has been loaded into python
```python
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
```

---
   3. Now, we are going to create a function to encrypt and decrypt using RSA. We take the plaintext and encrypt it using public key and OAEP padding. This is a secure padding method as it combined with SHA-256 hash to make encryption stronger. After we encrypted it, we are going to convert (encode) the ciphertext into base64 so it's easier to store. For the decryption, we reverse the process which mean, we decode the base64 to to it's original form (encrypted) then, we use the padding and private key to retrieve the original message. The last line is crucial since the decrypted result will be in bytes form we use the `**.decode('utf-8')**` to covert them to normal readable string.
   ---
```python

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
```
---
   4.  We are going to create different fucntion for encrypt and decrypt. If user choose to encrypt a message they require to type the message then provide receiver public key. once the key is loaded, the palintext will be encrypted and encode to base64. While if user decide to decrypt they require to upload or paste the ciphertext (one of the reason why we use base64) then provide the their private key.
   
```python
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

```
## Output🧪:
### 1️⃣ Invalid output

![alt text](</cryptography/Lab Works 20%25/Lab 4/evidence/rsa_encryption_output.png/invalid output.png>)


### 2️⃣ Encrypt file
![alt text](</cryptography/Lab Works 20%25/Lab 4/evidence/rsa_encryption_output.png/encrypt file.png>)

### 3️⃣ Decrypted file
![alt text](</cryptography/Lab Works 20%25/Lab 4/evidence/rsa_encryption_output.png/Sheba encrypted.png>)

---

## Task 3️⃣: Hashing (SHA-256)🧮
---
 1. First of all, create a file and write any message. Then, create a field for user to upload their file
![alt text](</cryptography/Lab Works 20%25/Lab 4/evidence/hashing_output.png/create .txt file.png>)

---
   2. Import required library. As for hashing we only need one which is the haslib
```python
import hashlib 
# Ask user to enter filename
filename = input("Enter the filename to hash: ")
```
---
   3. Next, we will open the fine in binary form and indicate them as f (this can be whatever you want). The file will be read first then hash using SHA-256 and the hash value will be stored in hexadecimal. Finally, the hash produced will be printed.
```python
try:
    with open(filename, "rb") as f:
        file_data = f.read()
        file_hash = hashlib.sha256(file_data).hexdigest()
        print("SHA-256 Hash of File:", file_hash)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
```
---
## Output
### 1️⃣ Without tampering

![alt text](/cryptography/Lab%20Works%2020%25/Lab%204/evidence/hashing_output.png/hashed.png)

### 2️⃣ After tampering

![alt text](</cryptography/Lab Works 20%25/Lab 4/evidence/hashing_output.png/after tampered.png>)

---
## Task4️⃣: Digital Signatures (RSA) 🧩
---
1. Like usual, the first thing we gotta do is import required library. It's like the ingredient in cooking. Without ingredient how are you gonna cook right? 😏
```python
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
```
---
   2. Now, we have to create e function for sign and verify. The sign function use private key to sign signature value from  a message. First, the message (plaintext) is converted in bytes since cryptography works in bytes. Then, SHA-256 will create hash value of the file and RSA will signed it with PKCS1v15 padding. The similar process occur in `verify_signature` function. The difference is only they will fetch the signature value from `sign_message` function.
   
```python
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
```
--- 
   3. We will create function to load the key. The script will open the key_file in binary form since PEM format contain special formatting despite look like text. Therefore, it is safer and more accurate to read them as raw bytes. `f.read()` will read the file content. `public_key = serialization.load_pem_public_key(f.read())
` will strips away the header/footer and decode the base64 so python can create a usable key object that will allow cryptography processes such as encryption and decryption.

```python
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
``` 
---
   4. Now, we will create a simple menu page that will let user to choose whether to sign of verify. If they choose to sign, they require to upload their private key then write the message. The `signature = sign_message(private_key, message)` will create the signature. The message and signature then will be save using the fucntion we have declared previously. The process for verifying is quite similar. Verifier need to upload the sender's public key. Then we will check if the sha and key is match, the signature is valid.
   
```python
def main():
    print("=== Digital Signature ===")
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
```
---
## Output 🥼🧪

### 1️⃣ Signed valid

![alt text](</cryptography/Lab Works 20%25/Lab 4/evidence/digital_signature_output.png/signed verified.png>)

### 2️⃣ Signed invalid

![alt text](</cryptography/Lab Works 20%25/Lab 4/evidence/digital_signature_output.png/signed fail.png>)
___
---
> Alhamdulillah, we have come to the end of the lab ❣️ I hope all of you enjoy and undestand this time walkthrough as it is quite heavy and dizzy since it full of python😵‍💫🌀.
>
> This may be my last lab work for this subject but In Shaa Allah I will keep updating interesting walkthrough of other activities. Bye and Assalamualaikum👋🏻😸
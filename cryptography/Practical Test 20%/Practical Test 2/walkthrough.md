## Assalamualaikum and Hi everyone 👋🏻
---

So this is my last assesment for this subject. For this last assignment we are going to spice things a little bit since we are going to conduct a malware analysis. 

> ⚠️The file run in this task is not real ransomware but it is a good practice to open any unknown `**.exe**` file in virtual environment This task should be conducted in VM so it will not affect your device

>🚨**IMPORTANT**: make sure you guys take a snapshot of the machine before you start execute any suspicious malicious file. So you can always revert back if the system crash 😨😵‍💫

Just fill the information needed and simply click the `take snapshot button`
![alt text](/Practical%20Test%2020%25/Practical%20Test%202/screenshot/snapshot.png)

To revert back the machine you can just simply choose and click `go to` button it will undo it back to the current state just like the snapshot you select

![alt text](/Practical%20Test%2020%25/Practical%20Test%202/screenshot/retrieve.png)

---

## Steps 🧩


## 1️⃣ Download file
![alt text](</Practical Test 20%25/Practical Test 2/screenshot/(1) download .exe file.png>)

After downloading any file from the internet, it is a good practice to check the hash value to ensure the file we receive is not tampered

    Get-FileHash <file_name>

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/(2) check hash value.png>)

> When download project from Github, always check the hash value since there are lots of malware in Github. Always be safe guys😉

You can paste the hash value in `virus total` app to check if the hash value has been assigned to any file. So like the file I use for this assignment, no file with the hash value are found

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/check hash in virus total.png>)

Use `Detect it Easy` to identify the programming language used. The simplest way is just drag and drop the file. It looks like this file is written in `python`

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/Identify programming language.png>)

---

## 2️⃣ Extract the file

---

The file we download just now is a zip file, therefore we need to extract it

Open the 7 Zip app. This app is a file archiver utility that allows user to:

- compress files
- extarct files
- craete password-protected archives
- open uncommon archive formats


![alt text](</Practical Test 20%25/Practical Test 2/screenshot/(3) extract the file.png>)

> Notice that, password are required to extracted it? It is because the owner of the file (in my case, my TTO) set a password on the file before compressing it

You cannot simply bypass or crack the password with the 7-Zip since the app is designed to proetct the file securely.

---

## 3️⃣ Execute the extracted file

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/(5) execute the file.png>)

There are three files in the folder

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/(6) file content.png>)

---

**Content of maklumat1.txt.enc**

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/(7) view maklumat 1.txt.png>)

---
**Content of maklumat2.txt.enc**

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/(8) view maklumat 2.txt.png>)

---

**Content of maklumat3.txt.enc**

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/(9) view malumat 3.txt.png>)

---

## 4️⃣ Decompile it to .pyc format

    pyinstxtractor <file_name>
    ls

Next, we are going to decompile it to `.pyc` file because this  format contain file such as bytecode

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/decompile to .pyc.png>)

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/check extracted file.png>)

    cd simulated_ransomware.exe_extracted
    ls

As you can see there are numerous file in the folder but our main focus is the `simulated_ransomware.pyc`. 

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/view content in folder.png>)

`.pyc` file is in in binary form hence it is not human -readable

    Get-Content <file_name.pyc>
![alt text](</Practical Test 20%25/Practical Test 2/screenshot/view .pyc file.png>)


---

## 5️⃣ Convert .pyc file to .py file

Like I said before, `.pyc` is not human-readble. So we need to convert it to `.py` format. 

    uncompyle6 (.pyc file) > (.py file)
    ls

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/convert to .py file.png>)

    uncompyle 6 <file_name>

![alt text](</Practical Test 20%25/Practical Test 2/screenshot/view .py.png>)

### Why convert `.pyc` to `.py`??? 🤔

Well it is simply because. `.py` format can

1. increase readability and understanding as it let you see original source code
2. enable modification and development. `.pyc` format will not allow you edit the file
3. Security analysis. As I mention before, `.pyc` is not human-readable, so analysing it totally impossible. (Unless you are 👽....JK =3). So change it to `.py` will help you able to read it and of course, analyse it

So what I can conclude is

- `.pyc` --> compiled bytecode, not human-firendly 😒
- `.py` --> source code, easy to read and edit 😄

---

## `.py` full code

```python
# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: simulated_ransomware.py
from Crypto.Cipher import AES
import os
from hashlib import sha256
KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[None[:16]]

def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len]) * pad_len


def encrypt_file(filepath):
    with open(filepath, "rb") as f:
        plaintext = f.read()
    padded = pad(plaintext)
    cipher = AES.new(KEY, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded)
    with open(filepath + ".enc", "wb") as f:
        f.write(ciphertext)
    os.remove(filepath)


if __name__ == "__main__":
    folder = "locked_files/"
    os.makedirs(folder, exist_ok=True)
    sample_files = [
     "maklumat1.txt", "maklumat2.txt", "maklumat3.txt"]
    contents = [
     "Assalamualaikum semua, pelajar kursus Cryptography semester 5.\nKeselamatan siber bergantung kepada kebijaksanaan anda dalam memahami kriptografi.\nGunakan ilmu ini untuk melindungi data, sistem, dan masa depan teknologi.\nJadilah perisai digital yang berintegriti dan berkemahiran.",
     "Setiap algoritma yang anda pelajari hari ini adalah benteng pertahanan esok.\nKuasa penyulitan (encryption) bukan hanya tentang kod, tetapi amanah dalam menjaga maklumat.\nTeruskan usaha, dunia digital menanti kepakaran anda!",
     "Semoga ilmu yang dipelajari menjadi manfaat kepada semua.\nGunakan kepakaran anda untuk kebaikan, bukan kemudaratan.\nSemoga berjaya di dunia dan akhirat!\n\nAdli, Lecturer Part Time, Feb-Mei 2025"]
    for name, content in zip(sample_files, contents):
        path = os.path.join(folder, name)
        with open(path, "w") as f:
            f.write(content)
        encrypt_file(path)
```

Now open your eyes guys 👀

In this `.py` file there are a number of crucial information that can be used to create a decryptor. Let's list it:

---

1. **Library and Algorithm**
   ```python
   from Crypto.Cipher import AES
   ```
   
     - this code use Crypto.Cipher from pcryptodome library
     - AES algorithm is used for encryption

---

2. **Hashing algorithm**
   ```python
   from hashlib import sha256
   ```
   - sha256 is used to generate key
  
  ---

3. **Key Derivation**
   ```python
   KEY_SUFFIX = "RahsiaLagi"
    KEY_STR = f"Bukan{KEY_SUFFIX}"
    KEY = sha256(KEY_STR.encode()).
    ```
    Pay close attention here. There are 2 variable hold the key value but the final value for the key is `BukanLagiRahsia`. The key then hashed by using the sha256 

---

Now, the padding part of the `.py` code need to be reverse. For example:

```python
def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len]) * pad_len
```
This is the initial `.py` code. As we an see  this function is add padding to fit the AES block size, therefore to decrypt it we need to remove the padding. So the code for decryptor will look like this instead

```python
def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]
```

---

Next, we are going to look at the encryption function and change to decrypt it.

```python
def encrypt_file(filepath):
    with open(filepath, "rb") as f:
        plaintext = f.read()
    padded = pad(plaintext)
    cipher = AES.new(KEY, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded)
    with open(filepath + ".enc", "wb") as f:
        f.write(ciphertext)
    os.remove(filepath)
```
Our decryptor file will look like this

```python
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
```

---

## Save file section

Encryption
```python
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
```

Decryption
```python
if __name__ == "__main__":
    folder = r"C:\Users\serim\Downloads\simulated_ransomware (1)\locked_files"
    for filename in os.listdir(folder):
        if filename.endswith(".enc"):
            full_path = os.path.join(folder, filename)
            decrypt_file(full_path)
```

Now that we have come to the end, let's do a bit flaw analysis 🕵🏻


1. Explain how and why the cryptography used in the ransomware is flawed

   - The simulated ransomware use AES encryption BUT in ECB mode with a hardcoded key🔑
   - ECB is a weak algorithm since it leak the pattern and hardcoded key is **DEFINITELY A `NO`, `NEIN`, `TIDAK`, `لا` 🙅🏻‍♂️**
  
        > hardcoded key means the encryption key is placed directly in the source code. So if attacker can gained `.py` file, they can get the key and create the decryptor

2. Suggest a more secure version of encryption could look like 
   
   - use a stronger algorithm such as AES instead of ECB. Like we has go several lab, AES is the current symmteric encryption algorithm used. Unlike ECB that leak the pattern, AES provide better encryption and authentication as it comes with IV
  
     > For those, who don't know IV, you guys can refer to my previous labwork😉
   - **DO NOT** hardcoded the key🔑
  
  ---

  That's all from me for this walkthrough. I hope you guys enjoy this assignment. In Shaa Allah, I will see you guys in other lab. 
  
  Assalamualaikum and have a good day 👋🏻🥰.
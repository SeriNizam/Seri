## Assalamualaikum and Hi everyone 👋🏻
---
Now that we have complete four lab task. It will be create to have and do revision about it. So for today, I am going to take you all to a walkthrough of similar process of what he have done in lab task before. Bismillah , let's start 💓!

---
---

### Task 1️⃣: Generate GPG Key Pair

If you remeber in the pervious, we use the openssl to create key. Now, we are going to use the gpg instead.

    gpg --full-key

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(1) use GPG.png>)

You then will be greted with a menu that require your input. Choose 1 to create RSA key pair. The click `enter`. Later, you will be asked a few question before the key published.

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(2) set key length.png>)

Set the key length to 4096. Notice the bracket mention `3072` key length. Why??? It is because the **minimum** RSA key size is 3072 bits but the longer the key size is recommended as it will be stronger. 

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(3) set period.png>)

Next, the system will ask for period of the key active. You can set it as long as you want but for this task, I am going to set it for 1 year. It will display the expired date and you need to confir

---
> 🚨 in Linux environment, when you see something like (y/N) the capital letter is the dominant choice which mean if you don't enter any input, It will assign the option with the upper case. So in this case, if you just simply press `enter` without any input, the system will assume the information is ❌🙅🏻‍♂️
  ---

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(4) create identity.png>)

Let's move on to the next question. You will need to fill up a few information such as:

- Real name (it don't have to be your real name. The system won't know what your real name😏🤪)
- Email address
- comment

Then, it will give you option if you want to make any changes to any information. You can just simply enter `O` if all the information has been fill correctly.

---
After you click `O`, a window will pop up asking you to assign a passphrase

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(5) creare passphrase.png>)

---
Re-type the passsphrase set for confirmation purpose

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(6) confirm passphrase.png>)

---
Finally, you can check on the key taht have been generated

    gpg --list-keys
![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(7) check key.png>)

---
## Task2️⃣: Encrypt and Decrypt a file
---

First of all, create a .txt file that contain message that need to be encrypted. There are multiple way to create file

    echo "<message>" >file_name.txt

```
vim file_name.txt
```

But for this walkthrough, I am going to use echo since it is easier.

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(8) create message.txt.png>)

---

Next, we will be encrypt the file

    gpg --output message.txt.gpg --encrypt --recipient "<email assigned in previous step>" message.txt

message.txt in the command above is my file name. Change it to your saved file name to perform this action.

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(10) encrypt message.txt.png>)

use `ls` to confirm the message has been successfully encrypted. The encrypted file will have the extension of `.gpg`

> 🚨friendly reminedr: Always remember to create a folder to store such thing else it will be messy like mine. It is because I forgot I am currently in home directory 🫠

---
The next step is to decrypt the file.

    gpg --output <decrypted_file_name.txt> --decrypt <encrypted_file_name.txt>
![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(11) decrypt message.txt.png>)

In my case, I want my dectpted file named as `decrypted_message.txt` and I previously saved my encryption file as `message.txt.gpg`. That is why my command in the picture looks like that. 

> Remember, if you have different named for your file, running my command used in picture will not work😉.

---

Once you click `enter` in the previous step, you are required to enter the passphrase that have been set earlier.

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(12) enter passphrase.png>)

Use the down arrow key on your keyboard to move to `ok` option. Press `enter`

---
If the passphrase enter is correct, the decrypted file will be viewed automatically
![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(13) final output.png>)

---

## Task3️⃣: Sign and verify a message

---
To start off, create a file to be signed. 

    echo "<message>" > signed_file_name.txt
![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(14) create signed.txt.png>)

You can verify the file existence by using `ls` command

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(15) verify with ls.png>)

> nyehehe~ I have create a folde of this task so it will not be a mess😄

    cat <file_name.txt>

to view the content of the file without opening it

![alt text](<//cryptography/Practical Test 20%25/Practical Test 1/screenshot/(16) view message.png>)

---

Now, we are going to signed the file using GPG. There are many method can be used to signed the file but I use the `--clearsign`

    gpg --clearsign <signed_message.txt>

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(17) sign the file.png>)

---
use the `ls` command to check the current content of our folder. Notice that there is a new file with `.asc` extension? That is the decrypted file
![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(18) check decrypted file.png>)

Next, we are going to verify the file

    gpg --verify signed_message.txt.asc

Then, you are required to insert the passphrase

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(18) enter passphrase.png>)

Then a mesage will appear after you enter the passphrase

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(19) verify.png>)

Don't worry. The message are dislpayed because we use `clearsign` which embeds the message and the signature together in `signed_message.txt.asc`. To view the plaintext just run:

    cat signed_message.txt.asc

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(20) view decrypted file.png>)

---

## Task4️⃣: Configure Passwordless SSH authentication

---

use the command `ip a` to check the machine ip address

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(20) check ip.png>)

---

Since I have enable ssh on my machine I will not be doing it again but I will provide steps for you guys

```
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable ssh
```

Then, check for ssh status

    sudo systectl start ssh

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(21) check ssh status.png>)

---

I want to ssh my vm (kali) using my localhost (window). So I will generate SSh key on window (my host)

    ssh-key -t -b 4096 "Seri Nizam-NWS23010057"

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(22) generate key on window.png>)

The system will ask for passsword, but since our goal is to make it passwordless, just press enter without any input

to view the key use:

    type $env:USERPROFILE\.ssh\id_rsa.pub

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(23) view key on window.png>)

---
Now, we are going to copy the public key to the vm. Turn on the VM and make a folder first

```
mkdir -p ~/.ssh
nano ~/.ssh/authorized_keys
```

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(24) create folder.png>)

---

Next, create a file to paste the key

    vim ~/.ssh/authorized_keys

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(25) create file.png>)

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(26) paste key in vm.png>)

Save and exit

---

Change the folder and file permission

```
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh

```
---

Let's test the connectivity now!

From window (host) use the ssh command

    ssh seri@192.168.48.142

> change seri to your user name and use your ip from the `ip a` command

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(28) Test connectivity.png>)

Notice that we don't need any password to get into vm. We can use `whoami` to verify current user

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(29) who am i output.png>)

---

Let's do more to prove we successfully ssh into the vm from localhost. If you are using window, open powershell and run these command

```
ssh seri@192.168.48.142 "echo NWS23010057 > seri.txt"
ssh seri@192.168.48.142 "cat seri.txt"
```

  >the first commadn is to create file while the second command is to view it

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(30)create file through window.png>)

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(31) view file in window.png>)

---

## Task5️⃣: Hash Cracking Challenge

---

Who loves cooking? Once thought of becoming a chef? **Meet CyberChef🧑🏻‍🍳!**


This one chef did not cook food — but it cooks data into something readable, crackable, and understandable! Whether it's encoding, decoding, or hash analysis, CyberChef helps slice and dice through complex formats like a pro. 🍽️🔐

---

For this task, wordlist and hashes will be provided

### **wordlists**
```
Bismillah
Assalamualaikum Semua
Apa Khabar Semuanya
Semoga Dalam Keadaan Sihat Hendaknya
Senang Je Soalan Ni Kaan
Tapi Kalau Susah
Begitulah Lumrah Kehidupan
Ada Yang Senaang
Ada Yang Susaaah
Apa2 Pun
Semoga Berjaya Semuanya
Alhamdulillah
Teruskan Usaha
Jangan Mudah Putus Asa
Setiap Cabaran Pasti Ada Hikmah
Percaya Diri Sendiri
Kejayaan Milik Yang Berusaha
Semoga Hari Ini
Lebih Baik Dari Semalam
InsyaAllah
```

### **hashes**

```
SnZlcmV4IEF2IEpmcmNyZSBFeiBCcnJl
7b77ca1e2b3e7228a82ecbc7ca0e6b52
e583cee9ab9d7626c970fd6e9938fcb2d06fbbd12f1c1a3c6902a215808c825c
```
---

### 🔎 Hash 1: `SnZlcmV4IEF2IEpmcmNyZSBFeiBCcnJl`

First, we need to identify the type of the hash and this is **not a hash** but base 64. We can determine the type by looking at the hash string itself. Base64 tend to have:

- use only uppercase, lowercase, numbers, +, / and sometime = which indicate a padding

So the characteristic is fullfill in this first hash string

Next, we are going to decode it using cyberchef🍳🧑🏻‍🍳. To use cyberchef, open your browser and search for `cyberchef`

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(33) decode.png>)

For first timer don't worry, it is quite simple:
- drag the `from base64` tab to the middle section. 
- on the last section you see there are two different area. Paste the input in the upper area the result will appear at the bottom area

But it still can't be read. Copy the output and open new browser. Search for `caesar cipher decoder`

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(34) caesar cipher.png>)

Paste the output before in the box, and click `decrypt` button. At the side, it will show output based on shifting so we can conclude the plaintext for the first hash is `Senang Je Soalan Ni Kaan`

---

### 🔎 Hash 2: `7b77ca1e2b3e7228a82ecbc7ca0e6b52`

Run the hash identifier tools in identify the type of hash then paste the hash value

    hash-identifier

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(35) identify hash Q2.png>)

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(36) craeate file.png>)

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(36) crack Q2.png>)

plaintext: Assalamualaikum Semua

---

### 🔎 Hash 3: `e583cee9ab9d7626c970fd6e9938fcb2d06fbbd12f1c1a3c6902a215808c825c`

Run the hash identifier tools in identify the type of hash then paste the hash value

    hash-identifier

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(37) identify hash Q3.png>)

![alt text](/cryptography/Practical%20Test%2020%25/Practical%20Test%201/screenshot/image.png)

![alt text](</cryptography/Practical Test 20%25/Practical Test 1/screenshot/(39) crack Q3.png>)
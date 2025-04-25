## Assalamualaikum and Hi Everyone 👋🏻

So this is my second lab work for this subject. For today, I am going to take you guys to a walkthrough of cryptographic attacks. You will learn how to crack weak password hashes and exploiting poor authentication in databases

>😱: Even hashed password can be cracked?!
>🕵🏻: It is weak my brother

So get ready detectives, prepare your investigation kit to hop on this investigation.

## Investigation Kit
| Tool | function |
| ---- | -------- |
| nmap | scan service on open port|
| john the ripper|  crack hashed password|
| hashid|  identify hash type|
|hasd-identifier|  identify hash type|


## 💻LAB TASK

### 1️⃣🔓Service enumeration and Initial Access

To begin, we will scan the target machine to identify service available on the open port. 
```sh
    nmap -sV <target-ip>
```
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/nmap%20scan.png)

That' a lot right! Grab your magnificient detective 🔍and look for database service running

There are 2 database service run on this target:

- mysql (port 3306)
- postgresql (port 5432)

>🏃🏻‍♂️but we will focus on mysql for this lab

Next, we will access the database from our localhost. Remeber, if you have no idea how to use the command just get the guide by using the command below

    mysql --help
    mysql -h <target-ip> -u <username> --skip-ssl



![alt text](<Screenshot 2025-04-25 112702.png>)
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/successful%20log%20in.png)
- -h : host
- -u : username
- --skip-ssl : to bypass disable the SSL service

and walla🪄 we are in the Database service now! 

>👀You know what is the best part?
😼 let's see the list of users and their password!

## 2️⃣Enumeration of users and Authentication Weakness

Database is the place to store data including user and password. Now that we are in it, let's see what treasure we can find.

    SHOW DATABASES;
- this command is use to list all the database in the service.
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/show%20database.png)

Then, we will infilitrate into mysql database

    use mysql
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/mysql.user.png)

Notice the bracket has change from none to mysql. That means we are now in mysql database

To identify tables in a database use this command
    SHOW TABLES;

![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/show%20tables.png)

The last table is user. We can assume all user's data is stored in here. Let's view the data

    SELECT user, Host, Password FROM user;

![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/view%20mysql.user.png)

😏Looks like these user didn't even have a password. They even have a weak access control

>🤔what does  % mean❓❓❓
- the % sign mean, they allow any IP to access them.

Moving on to the next step, we will attempt to authenticate using these accound.

    mysql -h 192.168.48.140 -u debian-sys-maint --skip -ssl

![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/debian%20log%20in.png)

    mysql -h 192.168.48.140 -u guest --skip-ssl

![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/guest%20login.png)

## 3️⃣🔎Password Hash Discovery and Hash Identification

Now, we need to look for tables that contain hash password. 

>😱: Isn't that mean we will view many output?!
😉: relax, we can just view the column and choose what column to view

    USE <database name>
    SHOW TABLES;
    DESCRIBE <table name>
So it will look like this
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/demo%20describe.png)

Therefore we can just simply choose to view the user and password
    SELECT user, password FROM users;
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/hash%20password.png)

Now that the password has been exposed but it is hashed. In cryptography, there are numerous type of hashing such as 

- MD5⚠️
- SHA-1⚠️
- SHA-2
  
>🚨Most of the hash mentioned above are deprecated. Currenly, we are using the SHA-256

Before we start cracking the password, it is important for us the identify the type. We can identify them
| Hash Function | Output Length         | Security Status     | Visual Characteristics                          | Use Cases & Notes                                |
|---------------|------------------------|----------------------|--------------------------------------------------|---------------------------------------------------|
| **MD5**        | 128 bits / 32 hex chars | ❌ Deprecated (weak) | - Lowercase hex only (0-9, a-f) <br> - Always 32 characters <br> - Looks compact | Fast, used in file checksums; vulnerable to collisions |
| **SHA-1**      | 160 bits / 40 hex chars | ❌ Deprecated (weak) | - Lowercase hex (0-9, a-f) <br> - 40 characters <br> - Longer and more “random-looking” than MD5 | Used in Git, certificates; broken (SHAttered attack) |
| **SHA-256**    | 256 bits / 64 hex chars | ✅ Secure            | - Lowercase hex (0-9, a-f) <br> - 64 characters <br> - More stretched and even-looking than MD5/SHA-1 | Used in SSL/TLS, blockchain, digital signatures |
| **SHA-512**    | 512 bits / 128 hex chars| ✅ Secure            | - Lowercase hex (0-9, a-f) <br> - 128 characters <br> - Very long, hard to mistake | Used in high-security systems, password hashing |

Let's look back at our hashed password
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/hashed%20password.png)

>🕵🏻💭 It is MD5 (weak! it's already outdated!)

To crack it:
1. save the hash password in a file
   
2. run the hash identification tools

To create new file, you can use command like nano or vim

    vim <file name.txt>
    or
    nano <filename.txt>

Then, use any identification tools (hashid or hash-identifier). For this walkthrough, I will show you how to use both of it

### a. hashid
using hashid is very simple! just type hashid and then hash value. So the command will look like this:
    
    hashid 5f4dcc3b5aa765d61d8327deb882cf99
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/hashid%201.png)
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/hashid2.png)
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/hashid%203.png)

### b. hash-identifier
type and run hash-identifier command to activate the tool. the, simply paste hash value

![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/hash%20identifier%201.png)
![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/hash%20identifier%202.png)

>🤔When I think back, it is actually the same. The difference is just the hash-identifier greet us with their bombastic banner. Don't you  think so?

The result show the probabilities of the hashed type. But the hash-identifier tell us which one has the highest possibilities and turns out MD5 is one of them. Congratulation on a spot on guess just know detectives!🎉

## 4️⃣👊🏻 Offline Hash Cracking
👀 is anyone name John here? If not we are safe because he is John the Ripper😱😨

But .....we need him to crack the hashed password so let's work with him.

    john --format=raw-md5 --wordlist=<wordlist.txt> <hash password file.txt>

![alt text](John.png)

and boom💥, there you can see the plaintext password


Before we proceed to challenges of this lab, let's answer a few question here


>1. Is accessing a database with no password a cryptographic failure? Explain how this violates secure cryptographic authentication principles
- Yes, accesing a database with no password constitutes a cryptographic failure since password is the fundamental method of authentication. They should ensure that system is accessed by authorized user only thus it break the authentication principle.

>2.  What cryptographic weaknesses exist in this hashing method?
- The hashing method used is MD5 which is already deprecated. MD5 is extrememly fast to compute. While this might sounds like an advantage (if it a CPU), it is actually a security flaw. Fast hashing dunctions are vulnerable to large-scale cracking attempts that mean it allow million or even billions attempt of password guess in a short amount of time.

## 😵‍💫💫Challenges encounter
As I do this lab, I have face a number of issues. I will park it here so that you guys can refer to it if you encounter the same problem.

![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/error%20connect%20ssh.png)
This problem occur due to imcompatible TLS/SSL version. We can solve this issue by disabling the SSL. They are plenty of command we can use. But I use the --skip-ssl. So the command I use to solve this issue is

    mysql -h <target-ip> -u <username> --skip-ssl

![alt text](/cryptography/Lab%20Works%2020%25/Lab%202/screenshots/Screenshots/error%20john.png)

This happen because we don't specify the type of hash. If we recall the moment we try to identify the type of hash using identifier tools, there are lot's of it right? Therefore John the ripper isn't sure which hashing algorithm to use. To fix this we use the  --format to specify the type of hash. The final command is:

    john --format=raw-md5 --wordlist=password.txt hashes.txt


## 🛡️Analysis and Mitigation
| **Issue**                                | **Description**                                                                                                                                                                      | **Proposed Secure Alternatives**                                                                                                                                                                               |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Authentication Flaws**                | - No password protection (anonymous login allowed for some MySQL users) <br> - Weak authentication mechanisms  | - Enforce **multi-factor authentication (MFA)** <br> - Implement **strong password policies** with complexity requirements                                                                                         |
| **Weak Password Hashing**               | - Use of **MD5** for password hashing <br> - MD5 is fast and vulnerable to **collision attacks**    | - usea more secure or current hashing type (e.g: sha256)                                          |
| **Transmission of Data**                | - Data (passwords, hashes) transmitted over unencrypted channels <br> - Lack of **SSL/TLS** protection exposes data to interception and tampering                                        | - Use **SSL/TLS** for encryption of data in transit <br> - Enforce **HTTPS** for web applications to secure data transmission <br> - Regularly review and update protocols to avoid vulnerabilities                   |
| **General Best Practices**              | - System may use outdated cryptographic algorithms <br> - Weaknesses in encryption and hashing could expose sensitive data or allow brute-force attacks                               | - Regularly **update software** and cryptographic protocols <br> - Conduct **penetration testing** and **security audits** to identify and mitigate weaknesses                                                     |


So that is the end of my labwork. I hope you guys enjoy my walkthrough and for those who try along, I hope you get the exact output like I did. That's all from me. Have fun and keep learning. See you in the next lab walkthrough. Bye!👋🏻

>مَنْ سَلَكَ طَرِيقًا يَلْتَمِسُ فِيهِ عِلْمًا، سَهَّلَ اللهُ لَهُ بِهِ طَرِيقًا إِلَى الْجَنَّةِ، وَمَا اجْتَمَعَ قَوْمٌ فِي بَيْتٍ مِنْ بُيُوتِ اللهِ، يَتْلُونَ كِتَابَ اللهِ، وَيَتَدَارَسُونَهُ بَيْنَهُمْ، إِلَّا نَزَلَتْ عَلَيْهِمِ السَّكِينَةُ، وَغَشِيَتْهُمُ الرَّحْمَةُ وَحَفَّتْهُمُ الْمَلَائِكَةُ، وَذَكَرَهُمُ اللهُ فِيمَنْ عِنْدَهُ
“Barangsiapa yang menempuh satu jalan untuk menuntut ilmu maka Allah SWT akan memudahkan baginya jalan untuk ke Syurga. Tidaklah satu kumpulan berkumpul di dalam sebuah rumah di antara rumah-rumah Allah, membaca kitab Allah (al-Qur’an) dan mempelajarinya sesama mereka melainkan akan turun kepada mereka sakinah (ketenangan), diliputi ke atas mereka rahmat dan dinaungi oleh malaikat serta Allah SWT akan menyebut mereka pada malaikat yang berada di sisi-Nya”. [Riwayat Muslim (4867)]






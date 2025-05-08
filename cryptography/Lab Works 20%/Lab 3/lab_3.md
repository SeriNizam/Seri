## Assalamualaikum and Hi Everyone👋🏻

It's good to see you back. For this labwork I am going to walkthrough you guys through symmetric, asymmetric, hashing and digital signature in cryptography. You can do this lab on your own but it will be more fun and engaging to have a friend with you so you can see how it work more clear. So get your friend and get ready to be secret message among you, spy!🕵🏻 

It is very simple to do it with your friend. You guys just follow this walkthrough and change your public key and encrypted file. How??? It's up to you. You can send it via whatsapp or wormhole. Bismillah, let's get started!

## Requirement
------------------------------
This lab need only a few tools:
|tool|function|
|-----|----------|
|openssl|to create key, encrypt and decrypt|
|sha256sum|to generate hashing|


 most of OS has install it by default but you can check it to be sure 
    
    openssl version
    sha256 --version
This will show the current version of the openssl and sha256sum. If there is no output produces, then that mean the tools is not installed and you need to install it

    sudo apt update
    sudo apt install openssl

And you good to go now

## 1️⃣ Symmetric Encryption and Decryption using AES-256-CBC
____________________________

1. Generate a strong, random key using openssl
   ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/generate random key (1).png>)

   To check or view the symmtric key. replace the <symmetric.key> with your key name
    
        cat <symmetric.key>
    
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/symmetric key 2.png>)

2. Create a .txt file with message to encrypt
    ![alt text](/cryptography/Lab%20Works%2020%25/Lab%203/screenshot/seri.txt.png)


3. use openssl enc to command to encrypt the message. We will use the AES-256-CBC algorithm
        
        openssl enc -aes-256-cbc -salt -in <file.txt> -out <file.enc> -pass file:./<symmetry.key>

    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/encrypt seri.txt (2).png>)

    >🚨You need to send the encrypted file to your friend and let them send theirs to you along with their public key. To encrypt your friend file, just put their file name instead of yours (the one you created)

4. Decrypt encrypted file using openssl
        
        openssl enc -d -aes-256-cbc -in <file.enc> -out <decrypt_file.txt> 
    
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/sheba decrypt.png>)

    Once the decryption complete, we can view the decrypted text

        cat <decrypted_file.txt> 
    ![alt text](/cryptography/Lab%20Works%2020%25/Lab%203/screenshot/view%20decrypt.png)
    
## 2️⃣ Asymmetric Encryption and Decryption using RSA

1. Generate RSA private key of at least 2048 bits with openssl

        openssl genpkey -algorithm RSA -out <private_key_name.key> rsa_keygen_bits:2048
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/generate RSA private key (6).png>)
To view generated private key, use:

        cat <private_key_name.key>
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/view RSA private key (7).png>)
    
2. Extract corresponding public key from the private key using openssl
   
        openssl rsa -pubout -in <private_key_name.key> -out <public_key_name.txt>
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/extract public key (8).png>)

3. Create a file and encrypt the message with  your friend public key

   ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/encrypt with pub sheba.png>)

4. Decrypt the file using private key with openssl

    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/decrypt sheba.png>)

## 3️⃣ Hashing and message integrity using SHA-256

1. create a .txt file with some content

        echo "write anything" > <file_name.txt>
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/create hashing_seri.txt (15).png>)

2. generate the sha-256 hash of the file.
   
   First method using openssl:

        openssl dgst -sha256 <hashed_file_name.txt>
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/hash hashing_seri.txt (16).png>)

    Second method using sha256sum

        sha256sum <hashed_file_named.txt>    
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/hashing (alternative way).png>)

    
3. Modify the content 
        
        sudo vim <hashed_file_name.txt>
   ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/modified hashing_seri.txt (17).png>)

   You can do anything whether delete a letter or add a space. After done modifying quit and exit


4. Generate the hash value of the modified file 

    >openssl:
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/new hash value (18).png>)
    sha256sum
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/new hash value (19).png>)

    >🚨notice that the value of the sha256 sum is different with the file before being edited. Different hash value mean the file has been tampered and integrity of CIA triad has been compromised!

## 4️⃣ Digital signature using RSA    
1. We are going to use the same RSA private key that has been generated in task 2
2. Create a .txt file that need to be signed

        echo "text here" > file_name.txt
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/create agreement.txt (20).png>)

3. Generate a digital signature for the file using our private key


        openssl dgst -sha256 -sign <private_key.key> -out <signed_file.txt> file_name.txt
   ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/signed agreement.txt (21).png>)
   ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/rename and verified (22).png>)

    >The verification output said okay which mean this file has been signed by the authorizes person and the content is not tampered.

4. Modify the content of the file and verify the original signature
   
        sudo vim <file_name.txt>
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/edit agreement.txt (23).png>)
    Exit and save

        openssl dgst -sha256 -verify <public_key.key> -signature <signed_file.txt> <file_name.txt>
    ![alt text](</cryptography/Lab Works 20%25/Lab 3/screenshot/verification fail (24).png>)
    
    > Verification fail because the file has been tampered. In digital signature, it protect the authenticity and integrity. With the file now being tampered, the integrity has been compromised.
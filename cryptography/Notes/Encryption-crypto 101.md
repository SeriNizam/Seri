# 101 crypto 

## key term
- ciphertext
  - result of encrypting a palintext, encrypted data
- cipher
  - a method of encrypting or decrypting data
- plaintext
  - data before encryption, often text but not always as it could be photograph or other file
- encryption
  - transforming data into ciphertext, using cipher
- encoding
  - not a form of encryption, just a form of data representation (e.g: base64)
- key
  - some information that is needed to correctly decrypt the ciphertextand obtain plaintext
- passphrase
  - separate to the key and simialr to password and used to protect key
- asymmetric encryption
  - use different key to encrypt and decrypt
- symmetric encryption
  - use same key to encrypt and decrypt
- brute force
  - attacking cryptography by trying every different password or every different key
- cryptanalysis
  - attacking cryptography by finding a weakness in the underlying maths

## importance of encryption
- cryptography is used to protect CIA
- SSL certificate is used to prove a valid bank user rather than a hacker
- use checksum to check downloaded file is right
- PCI-DSS state that the data shpuld be encrypted botha t rest in storage and while transmitted.

## Types of encryption
- symmetric
  - use same key to enncrypt and decrypt data
    - DES ⚠️
    - AES ✅
  - faster than asymmetric cryptography
  - use smaller keys 
    -  128 or 256 bit key are common for AES
    -  DES has 56 long key bits
- assymetric
  - use a pair of key to encrypt and decrypt data
    - RSA
    - Elliptic Curve Cryptography
  - key 
    - pulblic
    - private
  - private key encrypt data while public key decrypt data and vice versa.

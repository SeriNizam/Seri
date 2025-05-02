# 📚 Theory Test 1: Cryptography Revision

## 🔐 Modern Cryptography

Modern cryptography refers to the **advanced techniques and algorithms** used today to secure communication, data, and transactions in the digital world.

It relies heavily on **mathematics** and **computational complexity** to provide:
- **Confidentiality**
- **Integrity**
- **Authentication**
- **Non-repudiation**

Unlike traditional methods (e.g., Caesar cipher), modern cryptography is **robust, scalable, and secure** against brute-force and logical attacks.

---

## 🧠 Key Terms

| Term              | Description |
|------------------|-------------|
| **Plaintext**     | Original, readable data before encryption |
| **Ciphertext**    | Encrypted, unreadable version of data |
| **Encryption**    | Converting plaintext → ciphertext using a key |
| **Decryption**    | Converting ciphertext → plaintext using a key |
| **Key**           | A value used to encrypt/decrypt data |
| **Algorithm**     | A set of rules or formula for encryption/decryption |
| **Hashing**       | A one-way function that converts data into fixed-length hash (not reversible) |
| **Digital Signature** | A method to verify authenticity & integrity using asymmetric keys |
| **Public Key**    | Shared openly; used in encryption or signature verification |
| **Private Key**   | Kept secret; used in decryption or signing |
| **Non-repudiation** | Ensures sender cannot deny sending the message |
| **PKI**           | Public Key Infrastructure; system managing digital certificates |
| **CA**            | Certificate Authority; issues and verifies digital certificates |
| **SSL/TLS**       | Protocols that ensure encrypted communication over networks |

---

## 🔁 Symmetric Cryptography

- Uses the **same key** for both encryption and decryption
- Also known as **private key cryptography**
- Must keep the key **secret** between both parties

### ✅ Common Algorithms:
- **DES** (Data Encryption Standard) ⚠️ outdated
- **3DES** (Triple DES) ⚠️ legacy
- **AES** (Advanced Encryption Standard) – secure, widely used

### 🔒 AES Key Sizes:
- 128, 192, 256 bits (higher = stronger security)
- Fast and efficient, ideal for encrypting large amounts of data

---

## 🔀 Asymmetric Cryptography

- Uses a **key pair**: 
  - One key to encrypt
  - The other key to decrypt
- Also called **public key cryptography**
- Typically **slower** but more secure for key exchange and authentication

### ✅ Common Algorithms:

#### 🔐 RSA
- **Rivest-Shamir-Adleman**
- Used for secure transmission and **digital signatures**
- Public key encrypts, private key decrypts

#### 🧮 ECC (Elliptic Curve Cryptography)
- Uses elliptic curves over finite fields
- **Smaller key size**, **faster**, same security as RSA
- Great for **resource-constrained devices**

#### 🔐 DSA (Digital Signature Algorithm)
- Used for **digital signing only**
- Ensures message **authenticity and integrity**

---

## 🧾 Hashing (One-Way)

- **SHA (Secure Hash Algorithm)**
  - E.g., SHA-256, SHA-3
  - Used for:
    - Data integrity checks
    - Digital signatures
    - Password storage
    - Generating unique file IDs

---

## 🔑 Key Exchange Protocol

### 🔄 Diffie-Hellman (DH)
- Securely exchanges **symmetric keys** over a public network
- Prevents eavesdropping
- Often used **before symmetric encryption begins**

---

## 🗝️ Private Key vs Public Key Usage

### 🔐 In **Encryption/Decryption**:

| Action | Key Used | Who Holds It |
|--------|----------|---------------|
| Encrypt a message | Public Key (receiver's) | Sender |
| Decrypt a message | Private Key (receiver's) | Receiver |

### 🖊️ In **Digital Signatures**:

| Action | Key Used | Who Holds It |
|--------|----------|---------------|
| Sign a message | Private Key (sender's) | Sender |
| Verify signature | Public Key (sender's) | Receiver |

---

## ✉️ Digital Signatures

- Provide **authenticity** (who sent it) and **integrity** (not changed)
- Process:
  1. Sender creates a hash of the message
  2. Hash is **encrypted with sender’s private key** (signature)
  3. Receiver uses **sender’s public key** to verify

---

## 🌐 PKI, CA, SSL/TLS

### 🏛️ PKI (Public Key Infrastructure)
- Framework that uses digital certificates to manage keys
- Supports **secure online communication**

### 🧾 Certificate Authority (CA)
- Trusted entity that issues digital certificates
- Confirms the identity of organizations/individuals

### 🔐 SSL/TLS
- Protocols for encrypted client-server communication
- SSL = Secure Socket Layer
- TLS = Transport Layer Security (modern version)

---

## 🧠 Summary Table: Symmetric vs Asymmetric

| Feature | Symmetric | Asymmetric |
|--------|-----------|-------------|
| Keys Used | Same key | Public + Private key |
| Speed | Faster | Slower |
| Security | Key must be shared securely | No need to share private key |
| Used For | Encrypting bulk data | Secure key exchange, authentication |
| Examples | AES, DES | RSA, ECC, DSA |

---


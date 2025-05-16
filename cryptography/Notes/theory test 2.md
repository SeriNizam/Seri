# 📚 Cryptography Theory Notes (Clean & Exam Ready)

---

## 1️⃣ What is Cryptography?

- **Definition:** The science of securing information so only intended parties can understand or access it.
- **Main goals:**  
  - **C**onfidentiality → keep secret  
  - **I**ntegrity → detect tampering  
  - **A**uthentication → confirm identity  
  - **N**on-repudiation → prevent denial

---

## 2️⃣ Cryptography Types

| Type | Description | Example |
|------|-------------|---------|
| **Symmetric encryption** | Same key for encryption + decryption | AES, DES |
| **Asymmetric encryption** | Public key encrypts, private key decrypts | RSA, ECC |
| **Hashing** | One-way function to create fixed-size fingerprint | SHA-256, SHA-3 |
| **Digital Signatures** | Prove document authenticity & integrity | RSA signature, ECDSA |

---

## 3️⃣ Symmetric Encryption

- **One key** → both parties must share secret key securely
- **Fast**, used for **large data** encryption
- **Algorithms:** AES (Advanced Encryption Standard), ChaCha20

| Mode | Description | Safe? |
|------|-------------|-------|
| ECB | Same plaintext = same ciphertext | ❌ Insecure |
| CBC | Random IV, blocks chained | ✅ Secure (with random IV) |
| GCM | Encrypt + integrity check (AEAD) | ✅✅ Recommended |

---

## 4️⃣ Asymmetric Encryption

- **Key pair** →  
  📬 Public key (shared openly)  
  🔐 Private key (kept secret)

- **Public key encrypt → Private key decrypt**
- **Slower**, used for:
  - Encrypting small data (like AES keys)
  - **Digital signatures**
  - Secure key exchange (SSL/TLS)

- **Algorithms:** RSA, ECC (Elliptic Curve Cryptography)

---

## 5️⃣ Hashing

- **One-way** → irreversible
- **Fixed output** → no matter input size  
- **Avalanche effect** → small input change = big output change

- **Uses:**
  - Password storage
  - Integrity checks (file checksum)
  - Digital signatures

- **Algorithms:** MD5 (broken), SHA-1 (weak), **SHA-256**, **SHA-3**

---

## 6️⃣ Password Hashing (Khas Untuk Password)

- Regular hashes (MD5, SHA-1) are **too fast** → bad for passwords  
- Use **slow hashes** with salting

| Algorithm | Good? | Reason |
|-----------|-------|--------|
| MD5 | ❌ | Fast, crackable |
| SHA-1 | ❌ | Weak |
| bcrypt | ✅ | Slow, adaptive |
| PBKDF2 | ✅ | Slow, customizable |
| Argon2 | ✅✅ | Strongest, modern |

- **Salting** → random data added to password before hashing  
  (Prevents rainbow table attacks)

---

## 7️⃣ Digital Signatures

- Proves:
  - **Authenticity** (sender is real)
  - **Integrity** (message unchanged)
  - **Non-repudiation** (can't deny signing)

- Process:
  1. Hash the message
  2. Encrypt hash with **private key** (sign)
  3. Receiver decrypts signature with **public key** → compares hashes

- **Algorithms:** RSA signature, ECDSA

---

## 8️⃣ Key Exchange (Diffie-Hellman)

- Securely agree on a **shared key** over insecure channel
- No prior shared secret needed
- Basis of **TLS, VPNs**

---

## 9️⃣ Common Attacks

| Attack | Description | How to prevent |
|--------|-------------|----------------|
| Brute-force | Try all possible keys | Use long keys |
| Dictionary attack | Try common passwords | Strong, unique passwords |
| Man-in-the-middle | Intercept communication | Use encryption + authentication |
| Hash collision | 2 inputs = same hash | Use strong hash functions (SHA-256+) |
| Replay attack | Reuse valid data | Use **nonces**, timestamps |

---

## 🔟 Golden Rules for Secure Crypto

- Always **use strong algorithms** (AES-256, RSA-2048+, SHA-256+)
- **Never reuse IVs / nonces** in symmetric encryption
- **Protect your private key** (compromise = total failure)
- **Do not invent your own crypto algorithms** (use vetted ones)
- **Rotate keys periodically** to limit damage

---

## ✅ Exam Tips — If Time is Short

- Understand **symmetric vs asymmetric** (differences + examples)
- Know **hashing purpose** and **digital signature process**
- Remember **current best algorithms**:
  - AES-256
  - RSA-2048 or 4096
  - SHA-256 or SHA-3
  - bcrypt / Argon2 for passwords
- Understand **CIA (Confidentiality, Integrity, Authentication)** goals

---

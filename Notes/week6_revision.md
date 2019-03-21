# Revision

- [1. Ciphers](#ciphers)
- [2. Malware](#malware)
- [3. Digests](#digest-sizes)


## Ciphers
- Types:
    - Substitution
        - Ceasar (attack: O(26))
        - Vigenere (attack: O(26!))
        - Binary (attack: O(2^n))
    - Transposition
    - Modern:
        - Stream
        - Block


## Malware
- Types:
    - Virus
        - Spread through executable code
    - Worm
        - Spread through automated exploit over network
    - Adware
        - Download by user/browser for ads
    - Trojans
        - Hidden payload as part of the application
    - Rootkits/ Remote Access Tools
    - Ransomware
        - encrypts all files (holds them hostage)
        
## Digest Sizes:
- Input: 512 bits
    - MD5:
        - 128 bits
    - Sha-1: 80 rounds
        - 160 bits
    - Sha-2: 64 or 80 rounds
        - 224
        - 256
        - 384
        - 512
    - Sha-3: ??
        - arbitrary
        
## Commonly used primitives
- **One-way hash function**
    - sometimes also called as one-way compression function—compute a reduced hash value for a message 
    (e.g., SHA-256) Authentication
- **Symmetric key cryptography**
    - compute a ciphertext decodable with the same key used to encode (e.g., AES)
- **Public key cryptography**
    - compute a ciphertext decodable with a different key used to encode (e.g., RSA)
- **Digital signatures**
    - confirm the author of a message
- **Mix network**
    - pool communications from many users to anonymize what came from whom
- **Private information retrieval**
    - get database information without server knowing which item was requested
- **Commitment scheme**
    - allows one to commit to a chosen value while keeping it hidden to others, 
    with the ability to reveal it later
- **Cryptographically secure pseudorandom number generator**


## Questions for mid term
# Secure hash function

Authentication:
1. Identity authentication
    - identity of sender
2. Message authentication
    - valid message

- Design Challenge: Transparent Bidding
    - Assume n bidding
        - everyone can bid once
        - Bids are compared once all are given
        - Highest bid wins
    - Simpler: rock paper scissors game
    
- **IDEA**
    - Send msg digest(C) ahead first, then reveal.
    - This makes it possible to verify if the message has been changed
    - Compare if H(m) == C (sent ahead of time)
    
---
Message authentication codes (MAC)
---
- Introduce a key (secret)
- Makes it such that only actual sender can find hash
- Sent now contains (msg, tag): 
    - where tag = H(key, msg)
    - **note that key is symmetric**
    - Verifier will perform: H(k, m') == tag
    

- Vulnerabilities:
    - Attack 1: x = H(k, m)
        - find m' such that x = H(k,m||m')
        - first preimage attack 
    - Attack 2: x = H(m, k)
        - second preimage attack
    
    
---
Storage of secrets
---
- Security involves **redundancy**
- This is due to additional proof
- Rainbow tables can be used to direct map hashes to x


---
Collision Attacks
---
- Signing of good document with a matching malicious document
- Effort needed is **sqrt(2^n)** or **2^(n/2)**
    - where n is the number of bits in the document
- This can be applied to CA certificates


    
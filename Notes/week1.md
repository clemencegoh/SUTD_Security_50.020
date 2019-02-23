# Recap of network security
Updated: 23/2/2019 (Review)

---
- Basics:
    - **C**onfidentiality
        - obtaining secret data
    - **I**ntegrity
        - change data 
    - **A**vailability
        - avaiability of data (no DDOS)
    - **N**on-repudiation
        - once taken action, user cannot deny having taken it

- Privacy, Authenticity, Authentication:

| Privacy | Authenticity | Authentication |
| --- | --- | --- |
| user's personal data (similar to confidentiality) | Special case of integrity, where the reference version is at the state it was while under control of a specific entity | verify that user making request is valid |

---
How to measure security?
- Number of bugs in software
- Number of entry points
- Estimates based on complexity and cost

Feasibility of attack (bruteforce):
- Mathematically feasible
    - Possibility of attack
    - number of bugs
- Practically feasible
    - Time taken
        - complexity

**Important**:
- System can only be secure wrt well-defined assumptions/models.
    - System model with involved parties and their behaviour
    - Attacker model
    - List of requirements for operation of system, and security requirements
- Should be practically indecipherable, if not mathematically.
- Must not use obscurity as security (method cannot be hidden, only key)
- Key should be customizable and communicable without help of written notes

---     
Types of Disclosures:
1. Full Disclosure: Notify public immediately
2. No disclosure: Notify vendor, but no one else
3. Sell vulnerability on black market
4. Responsible disclosure: Notify producer of vulnerability, disclose to public after a certain set deadline

---
---
Lesson 2: Basics of substitution and transposition ciphers 
---

Ancient cipher
---

1. Caesar's cipher
    - Shift all characters by k in alphabet
    - total possibilities: 26 (or 25, exluding 0)
    - possible to crack through frequency analysis/brute force
    - Time taken: O(26) 
        - Realtime, easy for bruteforce.
2. Improved substitution cipher
    - map every character to a specific shift step (random mapping)
    - `{'a':2, 'b':4 ...}`
    - total number of possibilities: 26! (26 x 25 x...)
        - 2^88
    - **To attack, use frequency analysis and guesswork**
3. Advanced substitution:
    - Use dialect/intentionally misspell
    - Insert 'red herring' characters
    - Treat `et` as a new character, map to symbol `alpha`
4. Vigenere cipher (dead beef, key: 'CAB')
    - Also possible to use a "key word" to encode initial message
    - Based on 2d table
    - Follow the table and use the key word to add to the plaintext to form the ciphertext
    - new ciphertext based on 'dead beef' ==> 'febf bfgf' 
    - **To attack, 'brute force-ish'**: 
        - **Guess key length**
        - group 1's together, 2's together... Use as separate messages
        - try frequency analysis and get most frequent letter as 'e': must correspond to freq of english alphabet
        - key will be guessed from length and shift per message segment
5. Transposition cipher - change sequence only
    - **frequency analysis ineffective**
        - same letters, scrambled using key
        - Read using columns from initial plaintext
        - using the order of the letters in the key, display using columns
    - To attack: (will only work with simple cases)
        - Guess key length -> get the # rows 
            - max # row is from # letters / # columns

Modern cipher
---
1. Binary
    - Stream cipher
        - singular encoding (bit by bit)
        - low latency
        - cannot handle large throughput
    - Block cipher
        - encoding block by block
        - handles large throughput, parallel processing possible
        - padding required for missing bits of information
        
2. OTP - one time pad
    - **Brute force impossible**
    - Why?
        - 2^n possible plaintexts since there are 2^n keyspaces
        - Impossible to determine original plaintext
    - To generate key stream, a short key should be exchanged, then used to generate a long pseudo-random keystream sequence (must be as long as the plaintext).
    - Both parties generate this keystream separately to de/encrypt.
    - Generating function is public, but key stream must be unpredictable.
        



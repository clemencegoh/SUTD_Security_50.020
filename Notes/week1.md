# Recap of network security

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

- Others:
    - Non-repudiation
        - as above
    - Privacy
        - user's data (?) not sure exact diff between 
        this and confidentiality
    - Authenticity
        - verify that user making request is valid
---

Feasibility of attack:
- Mathematically feasible
    - Possibility of attack
    - number of bugs
- Practically feasible
    - Time taken
        - complexity
        
        
---
Lesson 2: Basics of substitution and transposition ciphers 
---

Ancient cipher
---

1. Caesar's cipher
    - Shift all characters by k in alphabet
    - total possibilities: 26 (or 25, exluding 0)
    - possible to crack through frequency analysis/brute force
2. Vigenere cipher
    - map every character to a specific shift step (random mapping)
    - `{'a':2, 'b':4 ...}`
    - total number of possibilities: 26! (26 x 25 x...)
    - **frequency analysis ineffective**
    - **To attack, use... ?**
        - first...
        
        ---
    - OR
    - Also possible to use a "key word" to encode initial message
    - **To attack, 'brute force-ish'**: 
        - **Guess key length**
        - group 1's together, 2's together... Use as separate messages
        - try frequency analysis and get most frequent letter as 'e': must correspond to freq of english alphabet
        - key will be guessed from length and shift per message segment
3. Transposition cipher - change sequence only
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
    - 
        



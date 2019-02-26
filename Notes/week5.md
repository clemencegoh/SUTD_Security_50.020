# Midterm exam: 1.20-2.50pm, march 7th, Cohort classroom 14 (2.507)

No new lecture next week

---
---

Operating Systems Security
---
To attack you need:
- Victim information
- Goal
- Payload that achieves the goal
- Attack vector for payload


Strategies:
- Social engineering 
- Emails
    - Can be used for phishing
    - Trick victim into visiting a website
    - *spearphishing*: targetting email phishing attempt
    - `Phishing is the fraudulent attempt to obtain sensitive 
    information such as usernames, 
    passwords and credit card details by disguising as 
    a trustworthy entity in an electronic communication.`
    - 

---
Buffer overflow:
-
- Exploit of Stack and Heap
- Can change both memory and instruction set


Countermeasures:
-
Secure coding practices
- Avoid insecure functions
    - https://github.com/intel/safestringlib/wiki/SDL-List-of-Banned-Functions
        
- **Canaries**
    - Canaries are random values saved just below RBP
    - before returning, OS will check if the canary is "alive" (still the same)
        - Can be random values
        - Checks if any of the canaries have **changed**
- Make the entire stack non-executable
    - **NX** bit, technology used in CPUs to **segregate** areas of memory
    for use by storage of processor instructions or for storage of data.
    - (More research needed, refer to slides from wk5-2)

- ASLR
    - Address Space Layout Randomization
    - Exploit mitigation, since attacker would need to know LibC base address
    

    
    
Malicious HowTo:
- 
- **NOT EASY**
    - Get address of OS function
    - Set up stack
    - return-to-LibC

- Procedural Linkage Table (PLT)
    - Used to direct executable's calls to LibC to dynamic address
    - No write permission into this
    - Instead of jumping into dynamic LibC address, jump into static **PLT**

    

(needs more elaboration)

---

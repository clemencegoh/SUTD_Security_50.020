# Rainbow table hash reverse report

Name: Clemence Goh (1002075)

---
- For 5 letter plaintext passwords and 6 letter salted passwords:

| Length of plaintext passwords | Number of rainbow tables used | Total time taken | 
| --- | --- | --- | 
| 5 | 3 | 8.61 s |
| 6 | 6 | 16.48 s |

The time taken for salted hashes are significantly longer,
since the is a need to look through permutations of 6 letters instead of 5.





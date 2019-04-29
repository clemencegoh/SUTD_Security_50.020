# Lab 12: ARP spoofing and TLS

## Part 1: Implement simple http-based messaging service
- Simple auth server without TLS implemented in app.py
- To test, use 
    - `username: guest`
    - `password: password` 
- Simple test to server is within studentclient.py


## Part 2 - securing http socket connection with TLS
- Generating Private Key:
    - `openssl genrsa -des3 -out server.key 1024`
- Generating CSR (Certificate Signing Request)
    - `openssl req -new -key server.key -out server.csr`
    

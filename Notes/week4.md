# Web security

Possible attacks
---
- Communication
    - Man-in-the-middle (strong attackers)
        - ISPs, Governments can eavesdrop or manipulate traffic
    - Normal hackers (scriptkiddies) not able to execute this kind of attack usually
- End hosts and Servers
    - Common attacks: Denial-of-Service [DOS] (Availability)
    - DDOS is Distributed DOS
    - Active attacks (sending user malicious traffic)
    - Passive attacks (tricking user into contacting attackers)

Prevention:
- Traffic attacks can be prevented by TLS (transport layer security)

Focus: Servers and end hosts
---
Definitions

| Terms | Definitions |
| --- | --- |
| Access control | Selective restriction of access to a place or some other resource |


Server:
- Weak access control 
- User-provided input
    - exploits that make use of this includes:
        - SQL Injection
        - Buffer overflow
        - Cross-Site-Scripting (XSS)
- DDOS

User PC-side:
- Execution of downloaded content
    - Impersonation of trusted sources to trick user into downloading
    - Downloaded content could contain a macro
- Accidental exposure of interfaces

User Accounts:
- Private Data
- Impersonation

---

Case study: Injection
---
Vulnerabilities:
- Buffer overflow
- **SQL Injection**
    - Why is this even possible?
    - Validation/sanitization of user inputs are not done properly
    - Usually makes use of escape characters like `'` or `--` (this is a comment in SQL)
    - Possible to extract entire table worth of data or manipulate data in table
- XSS
    - Particularly dangerous, since user-created content could potentially affect/target other users.
    - Code is executed by browser, and since it is on a known and trusted website, other users will trust the code and execute it.
    - Attack exploits user trust in server
    - Types:
        - Persistent/Second order XSS attacks
        - Reflected/First order XSS attacks
- Cross-Site request forgery (CSRF)
    - abuses server's trust in user
    - injects code via URL
    - Gets victim's browser to execute malicious code sent to them, which exposes their current connection to another party to the attacker. 
    - Seems uite similar to first order/reflected XSS

**Countermeasures**:
- SQL Injection:
    - Restrict/validate character set for values
        - eg. alphanum ONLY
    - Proper escape of special characters such as turning `'` into `"`, but troublesome.
    - Sematic analysis of query for execution
    - Restrict/disallow dropping of certain tables (control manipulation)
    - Use of prepared statements (with parameterized queries)
- XSS:
    - Again, possible to avoid by validation and escape of user input data.

---

How to increase effort for attacker?
---
Do something that is low effort for user, high effort for computer.
- Capchas
    - OCR made harder due to distorted images
    - However, prevents access for visually impaired
    - Could have low usability
- Client-side puzzle-solving (Proof-of-Work, Blockchain)


Improving capchas
- Use images
- 3D perceptions
- Knowledge associations
- etc.

---
---

# Lesson 2 - Web security II

Command Injection
---
Shellshock
- bash vulnerability, similar to SQL, escape char allows commands to be executed after the escape.
- Case study, *responsible disclosure* happened here.
- Example:
    -   ```
        env x='() { :;}; echo vulnerable' bash -c 'echo foo'
        ```
    - This caused 'vulnerable' to be echoed
- Could be used to:
    - ping back to attacker from victim
    - Open a reverse shell 
    - Download botnet client and join botnet

Reverse Shell
- Attack used when target machine is not directly reachable (behind firewall)
- By initiating contact, attacker will fail. However, by getting the victim to initiate contact, firewall will let the request go through. (Bind Shell VS Reverse Shell)
- Netcat is used for this.
- Attacker is listening to pings, picks up the shell.
- This shell can then be used to execute commands on the victim's machine.

---

# Server security

DDOS
---
Simple DOS uses ICMP ping flooding
- Target receives large number of pings, replies to each
- This requires a large amount of bandwidth on the attacker.
- DDOS allows multiple uplinks (where botnets are used or other users)
- Requires high amplification 
    1. DNS amplification
        - Ask for big DNS TXT resource record (~4kB) with 60B message
        - Set victim IP as source address
        - DNS will reply to victim.
        - Amplification is ~66x.

---

IoT malware
---
Mira case study: https://github.com/jgamblin/Mirai-Source-Code
- malware was spread amongst IoT devices
- Devices added to botnet
- Botnet used to launch massive DOS attacks

---

Cloud security
---
Heavily dependent on cloud provider.
## Part 4: Vulnapp

gdp output:
```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : disabled
PIE       : ENABLED
RELRO     : FULL
```

```
gdb-peda$ disass main
Dump of assembler code for function main:
   0x0000000000001192 <+0>:     push   rbp
   0x0000000000001193 <+1>:     mov    rbp,rsp
   0x0000000000001196 <+4>:     sub    rsp,0x40
   0x000000000000119a <+8>:     lea    rdi,[rip+0xe67]        # 0x2008
   0x00000000000011a1 <+15>:    call   0x1030 <puts@plt>
   0x00000000000011a6 <+20>:    lea    rax,[rbp-0x40]
   0x00000000000011aa <+24>:    mov    rdi,rax
   0x00000000000011ad <+27>:    call   0x1155 <getlines>
   0x00000000000011b2 <+32>:    lea    rax,[rbp-0x40]
   0x00000000000011b6 <+36>:    mov    rsi,rax
   0x00000000000011b9 <+39>:    lea    rdi,[rip+0xe7e]        # 0x203e
   0x00000000000011c0 <+46>:    mov    eax,0x0
   0x00000000000011c5 <+51>:    call   0x1040 <printf@plt>
   0x00000000000011ca <+56>:    mov    eax,0x0
   0x00000000000011cf <+61>:    leave  
   0x00000000000011d0 <+62>:    ret    
End of assembler dump.
```


RIP starts at position 72.
Follow this with 6 'E's.

---
Positions to note:
- printf: `0x7ffff7e2d8f0`
- pop rdi: `0x00007ffff7df705a`
- Register holding string: `0x555555559670` (probably wrong)

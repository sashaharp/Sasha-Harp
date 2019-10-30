global start

section .rodata
msg:        db      'Hello World!', 10
msglen:     equ     13

section .text
start:

            mov     rax, 1
            mov     rdi, 1
            mov     rsi, msg
            mov     rdx, msglen
            syscall
            mov     rax, 34
            syscall
            mov     rax, 60
            xor     rdi, rdi
            syscall
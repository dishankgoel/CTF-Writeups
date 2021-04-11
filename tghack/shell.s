[BITS 64]
global _start

_start:
	mov rdi, 42
	mov rax, 0x3c
	syscall

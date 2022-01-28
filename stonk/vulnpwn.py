#大神：https://ithelp.ithome.com.tw/articles/10281425
#pwntools: 我們用這個工具來接收/送出遠端連線的東西

#不要用pwn.py做檔名，會import錯
from pwn import *

#連接到指定port
r = remote('mercury.picoctf.net', 59616)
print(r.recvuntil(b'2) View my portfolio\n').decode())
# print(r.recvuntil(u'2) View my portfolio\n')) 
# 以上會跑出: BytesWarning: Text is not bytes; assuming ASCII, no guarantees.

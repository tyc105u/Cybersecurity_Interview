# https://ctftime.org/writeup/28915
'''
這題我們有c, n, 和e. 先分解n.
這邊有同行提點, 可以用FactorDB.
RSA介紹
但是C^d實在太大了, stack overflow有人說可以用3個augment => 相當於 x ^ y % z
'''
x = [1617549722683965197900599011412144490161, 475693130177488446807040098678772442581573]
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537
c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689

fn = (x[0]-1) * (x[1]-1)
#print(fn)

d = pow(e, -1, fn)
ans = pow(c, d, n)

#print(type(ans)) convert bytes to hex string
#print(hex(ans)) >>0x706...77d
#print(hex(ans)[2:]) >>706...77d [n:]去掉前n個數字
print(bytes.fromhex(hex(ans)[2:]).decode('ascii'))

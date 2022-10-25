from ast import For
from cmath import e
from re import A


p = 41 #input
q = 97 #input
e = 7 #input
m = (p-1) * (q-1)
loopNum = 10000 #integer 1 sampai 10000
kNum = 100 #k = 1, 2, 3 .... 100
k = []
for j in range(kNum):
    k.append(j)

for x in k:
    a = m * x
    for i in range (loopNum):
        if a == (e * i)-1 :
            # print(x);
            d = i
            
print('kunci privat(', e,  ',', m, ')')
print('kunci public(', d,  ',', m, ')')

    



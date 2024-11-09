import time
import sys
from charm.toolbox.pairinggroup import PairingGroup,ZR
from charm.toolbox.integergroup import RSAGroup
from charm.toolbox.integergroup import lcm,integer,toInt
from charm.toolbox.PKEnc import PKEnc
from charm.toolbox.hash_module import Hash


group = PairingGroup("SS512")

group2 = RSAGroup()
secparam=512
(p, q, n) = group2.paramgen(secparam)
n2=n**2
g=group2.random(n**2)
m=12345678901

# 两个ZR元素
element1 = group.random(ZR)
element2 = group.random(ZR)
toplus=0
tadd=0
texp=0
tmod=0
th=0
for i in range(1000):
    t1=time.perf_counter()
    int(element1) ^ int(element2)
    t2 = time.perf_counter()
    element2+element1
    t3 = time.perf_counter()
    g ** m
    t4 = time.perf_counter()
    g % n2
    t5 = time.perf_counter()
    #.hashToZn("asdfawerwagfsdfa")
    t6 = time.perf_counter()
    toplus+=(t2-t1)
    tadd+=(t3-t2)
    texp+=(t4-t3)
    tmod+=(t5-t4)
    th+=(t6-t5)
# 对两个ZR元素进行异或操作


# 打印结果
print(f"XOR: {toplus}")
print(f"Add: {tadd}")
print(f"g^m: {texp}")
print(f"g mod n^2: {tmod}")
print(f"h(): {th}")
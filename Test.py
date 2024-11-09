from charm.toolbox.pairinggroup import PairingGroup,G1,G2,GT,ZR,pair
import sys
import time

group=PairingGroup('MNT224')



zR=group.random(ZR)


P=group.random(G1)
Q=group.random(G2)
T=group.random(G1)

gT=group.random(GT)
Gt=group.random(GT)

i = 0
pa=0
sm=0
bp=0
ge=0
gm=0
hG=0
hZR=0
ra=0
rm=0
re=0
p=group.serialize(P)
sp=str(p)
for i in range(1000):
    t1 = time.perf_counter()
    # G1 point addtion
    P*T
    t2 = time.perf_counter()
    #scalar multiplication
    P ** zR
    t3 = time.perf_counter()
    #bilinear pairing
    gtt=pair(P,Q)
    t4 = time.perf_counter()
    #exp on GT
    gtt**zR
    t5 = time.perf_counter()
    #multi on GT
    gtt*gtt
    t6 = time.perf_counter()
    #Hash: {0,1}^* -> G1
    group.hash(zR, G1)
    t7 = time.perf_counter()
    #Hash:G1 to zr
    group.hash(sp,ZR)
    t8 = time.perf_counter()
    zR+zR
    t9 = time.perf_counter()
    zR*zR
    t10 = time.perf_counter()
    zR**zR
    t11 = time.perf_counter()
    pa += (t2 - t1)
    sm += (t3 - t2)
    bp += (t4 - t3)
    ge += (t5 - t4)
    gm += (t6 - t5)
    hG += (t7 - t6)
    hZR+=(t8-t7)
    ra += (t9-t8)
    rm += (t10-t9)
    re +=(t11-t10)
print("Point Addition",pa,"ms")
print("Scalar Multiplication",sm,"ms")
print("Bilinear Pairing",bp,"ms")
print("Exponentiation on GT",ge,"ms")
print("Multiplication on GT",gm,"ms")
print("Hash to Point",hG,"ms")
print("Hash to Integer",hZR,"ms")
print("Addition on ZR",ra,"ms")
print("Multiplication on ZR",rm,"ms")
print("Exponentiation on ZR",re,"ms")
print(gT)
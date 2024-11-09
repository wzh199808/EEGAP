from charm.toolbox.pairinggroup import PairingGroup,G1,G2,GT,ZR,pair
import sys
import time

group=PairingGroup('SS512')



zr=group.random(ZR)
P=group.random(G1)
gt=group.random(GT)

print(zr.bit_length())
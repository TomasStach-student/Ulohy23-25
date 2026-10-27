import random

loteria=[]
for i in range(6):
    loteria.append(random.randrange(1,50))
pocet={0:0,1:0,2:0,3:0,4:0,5:0,6:0}
spravne=0
file=open("loteria_2.txt","r")

for riadok in file:
    riadok=riadok.strip()
    typ=riadok.split(" ")
    for i in range(6):
        typ[i]=int(typ[i])
    for cislo in typ:
        if cislo in loteria:
            spravne+=1
    pocet[spravne]+=1
    spravne=0

print(f"1 spravne:{pocet[1]}\n2 spravne:{pocet[2]}\n3 spravne:{pocet[3]}\n5 spravne:{pocet[5]}\n6 spravne:{pocet[6]}")
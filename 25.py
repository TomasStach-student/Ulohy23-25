import random

zadanie=open

cisla=input("Zadaj cisla (odedelene medzerou):")
tip=cisla.split(" ")
c1=[]
for i in range(6):
    c1.append(random.randint(1,50))

print(c1)
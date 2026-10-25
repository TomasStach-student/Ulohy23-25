text=open("Sifra.txt", "r",encoding="utf-8")
final=open("Final.txt","w")
kluc=input("zadaj kluc:")
temp=""
tempsifra=""
posun=0
malaabc="abcdefghijklmnopqrstuvwxyz"

def sifruj():
    global text,final,kluc,temp,tempsifra
    for riadok in text:
        riadok = riadok.strip()
        temp += ((len(riadok) // (len(kluc))) * kluc)
        for i in range(0, len(riadok) % (len(kluc))):
            temp += kluc[i]

        for i in range(len(riadok)):
            if riadok[i] in malaabc:
                if (ord(riadok[i])+ord(temp[i])-ord("a")+1) <= ord("z") :
                    tempsifra+=chr(ord(riadok[i])+ord(temp[i])-ord("a")+1)
                else:
                    tempsifra+=chr(ord(riadok[i])+ord(temp[i])-122)

            else:
                tempsifra+=riadok[i]
        final.write(f"{tempsifra}\n")
        tempsifra=""
        temp = ""

    return final


def desifruj():
    global text,final,kluc,temp,tempsifra
    for riadok in text:
        riadok = riadok.strip()
        temp += ((len(riadok) // (len(kluc))) * kluc)
        for i in range(0, len(riadok) % (len(kluc))):
            temp += kluc[i]

        for i in range(len(riadok)):
            if riadok[i] in malaabc:
                if (ord(riadok[i]) - ord(temp[i]) + ord("a") - 1) >= ord("a"):
                    tempsifra += chr(ord(riadok[i]) - ord(temp[i]) + ord("a") - 1)
                else:
                    tempsifra += chr(ord(riadok[i]) - ord(temp[i]) + 122)
            else:
                tempsifra += riadok[i]
        final.write(f"{tempsifra}\n")
        tempsifra = ""
        temp = ""
    return final

desifruj()

text.close()
final.close()
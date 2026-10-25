import random

text = open("vstupny_text.txt", "r", encoding="utf-8")
final = open("zasifrovany_text_2.txt", "w", encoding="utf-8")

malaabc = "abcdefghijklmnopqrstuvwxyz"

vyber=input(f"Pre zasifrovanie zadajte '1', pre desifrovanie zadajte '2':")

def sifruj():
    global text, final, malaabc
    for riadok in text:
        riadok = riadok.strip()
        tempsifra = ""

        posun = random.randint(1, 25)

        pismeno_kluca = chr(posun + ord("a") - 1)
        tempsifra += pismeno_kluca

        for i in range(len(riadok)):
            if riadok[i] in malaabc:
                if (ord(riadok[i]) + posun) <= 122:
                    tempsifra += chr(ord(riadok[i]) + posun)
                else:
                    tempsifra += chr(ord(riadok[i]) + posun - 26)
            else:
                tempsifra += riadok[i]

        final.write(f"{tempsifra}\n")


def desifruj():
    global text, final, malaabc
    for riadok in text:
        riadok = riadok.strip()
        tempsifra = ""

        if len(riadok) == 0:
            continue

        pismeno_kluca = riadok[0]
        posun = ord(pismeno_kluca) - ord("a") + 1

        for i in range(1, len(riadok)):
            if riadok[i] in malaabc:
                if (ord(riadok[i]) - posun) >= 97:
                    tempsifra += chr(ord(riadok[i]) - posun)
                else:
                    tempsifra += chr(ord(riadok[i]) - posun + 26)
            else:
                tempsifra += riadok[i]

        final.write(f"{tempsifra}\n")

if vyber == "1":
    sifruj()
else:
    desifruj()

text.close()
final.close()

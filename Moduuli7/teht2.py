nimet = set()

while True:
    nimi = input("Syötä haluamasi nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi, syötä uusi nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Antamasi nimet ovat: ")
for i in nimet:
    print(i)

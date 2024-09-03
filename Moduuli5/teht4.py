kaupungit = []
#Käydään läpi 5 kertaa ja kysytään kaupungien nimet
for i in range (5):
    kaupunki = input("Syötä kaupunkisi nimen: ")
    kaupungit.append(kaupunki)
#Printataan lista kaupungeista
print("Antamasi kaupungit: ")
for kaupunki in kaupungit:
    print(kaupunki) 
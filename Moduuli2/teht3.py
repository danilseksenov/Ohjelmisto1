import math
korkeus = float(input("Anna korkeus (m): "))
kanta = float(input("Anna kanta (m): "))
#Lasketaan pinta-ala
area = korkeus * kanta
print(f"Suorakulmion pinta-ala on: {area:f}")
#Lasketaan piiri
circle = 2 * korkeus + 2 * kanta
print(f"Suorakulmion piiri on: {circle:f}")
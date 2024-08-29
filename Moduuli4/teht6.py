# Piin likiarvon laskeminen
# π≈4n/N, jossa n on yksikköympyrän sisälle osuvat pisteet, N on kaikki pisteet
# epäyhtälöllä x^2+y^2<1 testataan, onko yksittäinen piste ympyrän sisällä

import math
import random
counter = 0
N_count = int(input("Anna N arvo: "))
N = N_count #Pisteiden kokonaismäärä
n = 0 #Ympyrän sisään osuvat pisteet
while counter < N:
    counter = counter + 1
    # Arvotaan koordinaatit liukulukuina väliltä -1 ja 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Koordinaatiston piste: {x}, {y}")
    print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print("Osui ympyrän sisälle")
        n += 1
print(f"{N} pisteestä {n} osui yksikköympyrän sisälle")
result = 4 * n / N
print(f"Piin likiarvo on: {result}")
print(f"Virhe: {result -math.pi:.5f}")
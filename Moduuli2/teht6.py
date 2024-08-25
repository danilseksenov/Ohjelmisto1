import random

#3 numeroinen koodi
kolminumeroinen_koodi = "".join([str(random.randint(0, 9)) for _ in range(3)])
print(kolminumeroinen_koodi)

#4 numeroinen koodi
nelinumeroinen_koodi = "".join([str(random.randint(1, 6)) for _ in range(4)])
print(nelinumeroinen_koodi)
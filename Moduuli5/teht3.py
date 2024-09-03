tutkittava = int(input("Syötä tutkittava luku: "))

alkuluku = True

for jakaja in range(2, tutkittava):
    if tutkittava % jakaja == 0:
        alkuluku = False
        break

if alkuluku:
    print("Tutkittava lukusi on alkuluku")
else:
    print("Tutkittava lukusi ei ole alkuluku")
numbers = []

luku = input("Anna luku tai paina Enter lopettamiseksi: ")
while luku !="":
    numbers.append(int(luku))
    luku = input("Anna seuraava luku tai paina Enter lopettamiseksi: ")

numbers.sort(reverse = True)

print("Luvut suuruusjärjestyksessä suurimmasta alkaen: ")
for number in numbers [:5]:
    print(number)
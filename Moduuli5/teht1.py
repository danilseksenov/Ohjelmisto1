import random
n = int(input("Anna arpakuutioiden lukumäärä: "))

#Asetetaan alkusummaksi 0
summa = 0

#Asetetaan rajat
for i in range(n):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

#Tulostetaan noppien summa
print(f"Arpakuutioiden summa: {summa} ")
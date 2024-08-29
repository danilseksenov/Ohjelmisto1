import random
number_bycomp = random.randint(1,10)

while True:
    number_byplayer = int(input("Anna veikkaamasi numero: "))

    if number_byplayer < number_bycomp:
        print("Liian pieni arvaus!")
    elif number_byplayer > number_bycomp:
        print("Liian suuri arvaus!")
    else:
        print("Oikein!")
        break
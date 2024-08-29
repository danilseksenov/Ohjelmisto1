numero = []

while True:
    user_input = input("Anna luku: ")
    if user_input == "":
        break

    number = int(user_input)
    numero.append(number)

    print(number)
    print(f"Pienin luku: {min(numero)}")
    print(f"Suurin luku: {max(numero)}")
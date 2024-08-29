import math
while True:
    inch = float(input("Anna tuuma: "))
    centimeter = 2.54 * inch

    if inch < 0:
        print("Toiminta lopetettu!")
        break
    print(f"{inch} tuumaa on {centimeter:.2f} senttimetriä")

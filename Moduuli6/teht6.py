import math
def calculate_price(diameter, price):
    #muutetaan senttimetrit metreiksi
    diameter = diameter/ 100
    #pizzan pinta-ala pi*r**2
    r = diameter/2
    area = math.pi*r**2
    return price/area

pizza1_diameter = float(input("Syötä 1. pizzan halkaisija (cm): "))
pizza2_diameter = float(input("Syötä 2. pizzan halkaisija (cm): "))

pizza1_price = float(input("Syötä 1. pizzan hinta: "))
pizza2_price = float(input("Syötä 2. pizzan hinta: "))

pizza1_calculate_prize = calculate_price(pizza1_diameter, pizza1_price)
pizza2_calculate_prize = calculate_price(pizza2_diameter, pizza2_price)

print(f"1. pizzan neliöhinta on {pizza1_calculate_prize:.2f}")
print(f"2. pizzan neliöhinta on {pizza2_calculate_prize:.2f}")

if pizza1_calculate_prize < pizza2_calculate_prize:
    print("1. pizza on neliöhinnaltaan halvempi")
elif pizza1_calculate_prize > pizza2_calculate_prize:
    print("2. pizza on neliöhinnaltaan halvempi")
else:
    print("Pizzojen neliöhinta on sama.")
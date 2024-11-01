import random

from tabulate import tabulate

class Auto:
    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.atm_speed = 0
        self.distance = 0

    def accelerate(self, speed_diff):
        #Uusi nopeus
        new_speed = self.atm_speed + speed_diff

        if new_speed > self.max_speed:
            self.atm_speed = self.max_speed
        elif new_speed < 0:
            self.atm_speed = 0
        else:
            self.atm_speed = new_speed

    def travel(self, hours):
        distance = self.atm_speed * hours
        self.distance += distance

autot = []
for i in range (1,11):
    plate = f"ABC-{i}"
    max_speed = random.randint(100,200)
    auto = Auto(plate, max_speed)
    autot.append(auto)

#kilpailu
competition_continues = True
while competition_continues:
    #Arvotaan nopeuden muutos
    for auto in autot:
        speed_change = random.randint(-10, 15)
        auto.accelerate(speed_change)

    #liikutaan tunnin ajan
    for auto in autot:
        auto.travel(1)

    #tarkistus, jos jokin auto ylitti 10000 km
    for auto in autot:
        if auto.distance >= 10000:
            competition_continues = False
            break

table_data = []
for auto in autot:
    table_data.append([auto.plate, auto.max_speed, auto.atm_speed, f"{auto.distance:.2f}"])

headers = ["Rekisteritunnus", "Huippunopeus (km/h)", "Nykyinen nopeus (km/h)", "Kuljettu matka (km)"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))
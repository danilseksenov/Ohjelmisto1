import random
from tabulate import tabulate

class Auto:
    def __init__(self, plate, max_speed):
        self.nimi = plate
        self.huippunopeus = max_speed
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, speed_diff):
        #Uusi nopeus
        new_speed = self.nopeus + speed_diff

        if new_speed > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif new_speed < 0:
            self.nopeus = 0
        else:
            self.nopeus = new_speed

    def kulje(self, hours):
        distance = self.nopeus * hours
        self.matka += distance

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10,15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nTilanne - {self.nimi} kilpailu")
        print("-" * 40)
        print(f"{'Auto':<15}{'Nopeus (km/h)':<15}{'Matka (km)':<10}")
        print("-" * 40)
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.nopeus:<15}{auto.matka:<10}")
        print("-" * 40)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus_km:
                return True
        return False

def luo_autot():
    autot = [
        Auto("Auto 1", 180),
        Auto("Auto 2", 200),
        Auto("Auto 3", 220),
        Auto("Auto 4", 210),
        Auto("Auto 5", 195),
        Auto("Auto 6", 180),
        Auto("Auto 7", 205),
        Auto("Auto 8", 190),
        Auto("Auto 9", 200),
        Auto("Auto 10", 215)
    ]
    return autot

autot = luo_autot()
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

print("\nKilpailu on päättynyt!")
kilpailu.tulosta_tilanne()
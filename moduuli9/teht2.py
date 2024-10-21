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

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {auto.plate} ja maksiminopeus: {auto.max_speed} km/h")
print(f"Auton tämänhetkinen nopeus: {auto.atm_speed} km/h ja kuljettu matka: {auto.distance} km")

#Kiihdytetään
auto.accelerate(30)
auto.accelerate(70)
auto.accelerate(50)
print(f"Auton tämänhetkinen nopeus: {auto.atm_speed} km/h")
#hätäjarrutus
auto.accelerate(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.atm_speed} km/h")

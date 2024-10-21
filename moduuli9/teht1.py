class Auto:
    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.atm_speed = 0
        self.distance = 0

auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {auto.plate} ja maksiminopeus: {auto.max_speed} km/h")
print(f"Auton tämänhetkinen nopeus: {auto.atm_speed} km/h ja kuljettu matka: {auto.distance} km")
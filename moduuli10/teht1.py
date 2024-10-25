class Hissi:
    def __init__(self,alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin_kerros or kohde_kerros < self.alin_kerros:
            print(f"Kerrosta {kohde_kerros} ei ole olemassa!")
            return
        if self.nykyinen_kerros < kohde_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
        if self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros == self.ylin_kerros:
            print("Olet saavuttanut ylimmän kerroksen!")
            return
        self.nykyinen_kerros += 1
        print(f"Nykyinen kerroksesi on: {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros == self.alin_kerros:
            print("Alin kerros on saavutettu!")
            return
        self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros on: {self.nykyinen_kerros}")

hissi = Hissi(1,9)
hissi.kerros_ylos()
hissi.kerros_ylos()
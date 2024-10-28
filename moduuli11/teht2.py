class Auto:
    def __init__(self, kilpi, maksiminopeus):
        self.kilpi = kilpi
        self.maksiminopeus = maksiminopeus
        self.nopeus = 0
        self.matka = 0

    def kulje(self, tunnit):
        matka = self.nopeus * tunnit
        self.matka += matka

    def aseta_nopeus(self, nopeus):
        self.nopeus = nopeus

    def tulosta_matkamittari(self):
        print(f"Auton {self.kilpi} matkamittarilukema on: {self.matka} km")

class Sahkoauto(Auto):
    def __init__(self, kilpi, maksiminopeus, kWh):
        super().__init__(kilpi, maksiminopeus)
        self.kWh = kWh

class Polttomoottoriauto(Auto):
    def __init__(self, kilpi, maksiminopeus, litrat):
        super().__init__(kilpi, maksiminopeus)
        self.litrat = litrat

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

#asetetaan nopeus
sahkoauto.aseta_nopeus(120)
polttomoottoriauto.aseta_nopeus(150)

#käsketään ajamaan
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

#tulostetaan matkamittarilukemat
sahkoauto.tulosta_matkamittari()
polttomoottoriauto.tulosta_matkamittari()
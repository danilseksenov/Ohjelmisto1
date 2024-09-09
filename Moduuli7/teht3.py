lentoasematiedot = {
    "EFHK": "Helsinki-Vantaa (Suomi)",
    "EGLL": "Lontoo-Heathrow (Iso-Britannia)",
    "LFPG": "Pariisi-Charles de Gaulle (Ranska)",
    "EDDF": "Frankfurt am Main (Saksa)",
    "EHAM": "Amsterdam Schiphol (Alankomaat)",
    "LEMD": "Madrid-Barajas (Espanja)",
    "LIRF": "Rooma-Fiumicino (Italia)",
    "EKCH": "Kööpenhamina-Kastrup (Tanska)",
    "LOWW": "Wien-Schwechat (Itävalta)",
    "LSZH": "Zürich (Sveitsi)"
    }

def syota_lentokentta(lentoasematiedot):
    icao_koodi = input ("Anna ICAO- koodi: ").upper()
    lentoaseman_nimi = input ("Anna lentoaseman nimi:  ")
    lentoasematiedot[icao_koodi] = lentoaseman_nimi
    print(f"Lentoasema {lentoaseman_nimi} (ICAO: {icao_koodi}) lisätty lentoasematietoihin")

def hae_lentokentta(lentoasematiedot):
    icao_koodi = input ("Anna ICAO- koodi: ").upper()
    if icao_koodi in lentoasematiedot:
        print(f"Lentoaseman nimi {lentoasematiedot[icao_koodi]}")
    else:
        print("Kyseisellä ICAO- koodilla ei löydy lentokenttää!")

while True:
    print("Valitse seuraava toiminto: "
          " \n1 - Syötä uusi lentokenttä "
          " \n2 - Hae lentokenttä "
          " \n3 - Lopeta ")

    vaihtoehto = int(input("Valitse toiminto (1-3): "))
    if vaihtoehto == 1:
        syota_lentokentta(lentoasematiedot)

    elif vaihtoehto == 2:
        hae_lentokentta(lentoasematiedot)

    elif vaihtoehto == 3:
        print("Toiminto lopetetaan")
        break
    else:
        print("Virheellinen toiminto, kokeile uudestaan!")
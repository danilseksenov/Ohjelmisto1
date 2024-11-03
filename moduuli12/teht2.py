import requests


def hae_saa(paikkakunta):
    # OpenWeather API -avain
    api_key = "c2f8e33b5ef650f12710dd8433fad086"

    # Määritellään URL ja parametrit
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": paikkakunta,
        "appid": api_key,
        "lang": "fi"  # Kielikoodi suomeksi
    }

    # Lähetetään pyyntö OpenWeather API:lle
    response = requests.get(url, params=params)

    # Tarkistetaan, onnistuiko pyyntö
    if response.status_code == 200:
        data = response.json()

        # Haetaan sääkuvaus ja lämpötila (Kelvininä)
        saakuvaus = data["weather"][0]["description"]
        lampotila_kelvin = data["main"]["temp"]

        # Muutetaan Kelvin-asteet Celsius-asteiksi
        lampotila_celsius = lampotila_kelvin - 273.15

        # Tulostetaan säätilan tiedot
        print(f"Sää paikkakunnalla {paikkakunta}: {saakuvaus.capitalize()}")
        print(f"Lämpötila: {lampotila_celsius:.2f} °C")
    else:
        print("Säätietojen hakeminen epäonnistui. Tarkista paikkakunta tai API-avain.")


# Kysytään käyttäjältä paikkakunta
paikkakunta = input("Anna paikkakunnan nimi: ")

# Kutsutaan sääkyselyfunktiota
hae_saa(paikkakunta)

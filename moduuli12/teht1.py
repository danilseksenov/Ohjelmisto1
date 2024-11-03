import requests
import json

def get_joke():
    base_url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(base_url)
        joke = response.json().get("value")
        print(joke)
    except requests.exceptions.RequestException as e:
        print("Virhe vitsiä haettaessa")

get_joke()

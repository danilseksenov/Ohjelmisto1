import random
def tahkojen_yhteismaara(tahkot):
    return random.randint(1, tahkot)

def main():
    maxsilmaluku = int(input("Syötä maksimisilmäluku: "))
    while True:
        tulos = tahkojen_yhteismaara(maxsilmaluku)
        print(f"Silmäluku on: {tulos}")
        if tulos == maxsilmaluku:
            break
main()
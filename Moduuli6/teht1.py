import random
def nopan_silmaluku():
    return random.randint(1,6)

def main():
    while True:
        tulos = nopan_silmaluku()
        print(f"Silmäluku on: {tulos}")
        if tulos == 6:
            break

main()
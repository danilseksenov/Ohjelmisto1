def gallonat_litroiksi(gallona):
    return gallona * 3.785

while True:
    gallonamaara = int(input("Syötä gallonamäärä: "))
    litrat = gallonat_litroiksi(gallonamaara)
    print(f"{gallonamaara} gallonaa on {litrat:.3f} litraa.")
    if gallonamaara < 0:
        break



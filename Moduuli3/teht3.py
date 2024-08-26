#Kysytään käyttäjän sukupuoli ja hemoglobiiniarvo

sukupuoli = input("Anna sukupuoli (mies/nainen): ")
arvo = int(input("Anna arvo (g/l): "))

if sukupuoli == "mies":
    if arvo < 134:
        print("Hemoglobiini arvosi on liian alhainen")
    elif arvo <= 195:
        print("Hemoglobiini arvosi on normaali")
    else:
        print("Hemoglobiini arvosi on korkea")

if sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiini arvosi on liian alhainen")
    elif arvo <= 175:
        print("Hemoglobiini arvosi on normaali")
    else:
        print("Hemoglobiini arvosi on korkea")
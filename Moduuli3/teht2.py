#Kysytään hyttiluokkaa
hyttiluokka = input("Anna hyttiluokkasi (LUX, A, B, C): ")

if hyttiluokka == "LUX":
    print("Parvekkeellinen hytti yläkannella")
elif hyttiluokka == "A":
    print("Ikkunallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print("Ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print("Ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")

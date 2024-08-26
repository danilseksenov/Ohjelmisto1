#Kysytään kuhan pituutta
kuhan_pituus = float(input("Anna kuhan pituus (cm):"))
#Kuhan alamitta:
kuhan_alamitta = 37.0

if kuhan_pituus < kuhan_alamitta:
    puuttuva_pituus = kuhan_alamitta - kuhan_pituus
    print(f"Kuha on alamittainen laske veteen!"
           f"Kuhalta puuttuu {puuttuva_pituus:.1f} cm")
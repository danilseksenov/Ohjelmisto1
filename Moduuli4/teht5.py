right_login = "python"
right_password = "rules"
rep = 0
while rep<5:
    user_login = str(input("Syötä käyttäjätunnus: "))
    user_password = str(input("Syötä salasana: "))

    if user_login == right_login and user_password == right_password:
        print("Tervetuloa!")
        break
    else:
        rep +=1
        if rep < 5:
            print("Virheellinen käyttäjätunnus tai salasana. Yritä uudelleen.")

if rep == 5:
    print("Pääsy evätty!")



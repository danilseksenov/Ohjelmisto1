talvi = (12,1,2)
kevat = (3,4,5)
kesa = (6,7,8)
syksy = (9,10,11)

vuodenaika = int(input("Syötä haluamasi kuukausi numerona: "))

if vuodenaika in talvi:
    print("Vuodenaika on talvi")
elif vuodenaika in kevat:
    print("Vuodenaika on kevät")
elif vuodenaika in kesa:
    print("Vuodenaika on kesä")
else:
    print("Vuodenaika on syksy")




while True:
    PriskWh = 1.255
    inköpsprisNy = input("Skriv inköpspriset: ")
    inköpsprisNy = float(inköpsprisNy)

    elGammal = input("Skriv elförbrukningen för den gamla apparaten i kwh: ")
    elGammal = float(elGammal)

    elNy = input("Skriv elförbrukningen för den nya apparaten i kwh: ")
    elNy = float(elNy)

    MinDag = input("Skriv hur många minuter om dagen apparaten används: ")
    MinDag = float(MinDag)

    if elGammal - elNy <= 0:
        print("Det kommer inte löna sig att köpa en ny apparat.")
        continue
    
    elDiff = elGammal - elNy

    HDag = 60/MinDag

    HÅr = HDag * 365

    PrisÅr = HÅr * elDiff * PriskWh

    År = inköpsprisNy/PrisÅr
    År = str(År)

    print("Det kommer att löna sig om " + År + "år")
    break
    








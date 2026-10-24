pareiza_parole = "Python123"
meginajumi = 0
maks_meginajumi = 3

while meginajumi < maks_meginajumi:
    parole = input("Ievadi paroli: ")

    if parole == pareiza_parole:
        print("Piekļuve atļauta")
        break
    else:
        meginajumi = meginajumi + 1
        atlicis = maks_meginajumi - meginajumi

        if atlicis > 0:
            print(f"Nepareiza parole. Atlikuši mēģinājumi: {atlicis}")
        else:
            print("Piekļuve bloķēta")

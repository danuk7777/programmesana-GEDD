
try:
    n = int(input("Ievadi pozitīvu veselu skaitli n: "))

    if n <= 0:
        print("Kļūda: skaitlim jābūt lielākam par 0.")
    else:
        summa = 0

        for skaitlis in range(1, n + 1):
            summa = summa + skaitlis

        print("Summa no 1 līdz", n, "ir", summa)

except ValueError:
    print("Kļūda: jāievada vesels skaitlis.")

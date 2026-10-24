vecums = int(input("Ievadi savu vecumu: "))

if vecums < 0:
    print("Vecums nevar būt negatīvs!")
elif vecums <= 12:
    print("Tu esi bērns")
elif vecums <= 17:
    print("Tu esi pusaudzis")
elif vecums <= 64:
    print("Tu esi pieaugušais")
else:
    print("Tu esi seniors")

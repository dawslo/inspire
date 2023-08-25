# Spør om første dato og måned

day1 = int(input("Skriv inn første dato: "))
mo1 = int(input("Skriv inn første månned: "))

# Spør om andre dato og måned

day2 = int(input("Skriv inn andre dato: "))
mo2 = int(input("Skriv inn andre månned: "))

# Variabler med tekst for å skrive mindre kode

rr = "Riktig rekkefølge!"
fr = "Feil rekkefølge"

# Sjekker rekkefølge

if mo1 < mo2:
    print(rr)
    
elif mo1 > mo2:
    print(fr)

else:
    if day1 < day2:
        print(rr)
    elif day1 > day2:
        print(fr)
    else: 
        print("Samme dato!")


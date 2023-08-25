# Informerer brukeren om forventa format

print("SKriv inn datoen som MMDD \nEksempel: 4 Februar = 0204")

# Spør om daotene
date = int(input("Skriv inn første dato: "))
date2 = int(input("SKriv inn andre dato: "))

# Sjekker rekkefølge

if date < date2:
    print("Riktig rekkefølge!")
elif date > date2:
    print("Feil rekkefølge!")
else:
    print("Samme dato!")



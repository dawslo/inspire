#Oppgave 14 - Repetisjon

# 1) Lag en tom liste mineOrd
mineOrd = []

# 2) Definer en funksjon som heter slaaSammen. Funksjonen skal ta imot to strenger, konkatenere dem (slå dem sammen) og returnere den sammenslåtte verdien.
def slaaSammen(tekst1, tekst2):
    return tekst1 + tekst2

# 3) Definer en prosedyre som heter skrivUt. Prosedyren skal ta imot en liste og skrive ut hvert element i listen på hver sin linje ved hjelp av en for-løkke.
def skrivUtListe(liste):
    for tekst in liste:
        print(tekst)

# 4) Lag en variabel valg som tar imot input fra brukeren. Spør brukeren om han/hun vil fortsette, legge til tekst eller skrive ut listen.
valg = input("Skriv i for å legge til tekst, u for å skrive ut listen, eller s for å avslutte: ")

# 4a) Hvis brukeren skriver inn ”i” skal programmet be om to tekststrenger og deretter kalle på funksjonen slaaSammen med disse som parametere. 
while valg == "i" or valg == "u" or valg == "s":

    # 4b) Hvis brukeren skriver inn ”u” skal du kalle prosedyren skrivUt med mineOrd som parameter. 
    if valg == "i":
        tekst1 = input("Skriv inn en tekst: ")
        tekst2 = input("Skriv inn en tekst til: ")
        mineOrd.append(slaaSammen(tekst1, tekst2))

    elif valg == "u":
        skrivUtListe(mineOrd)

    # 4c) Hvis brukeren skriver inn ”s” skal vi gå ut av løkken og avslutte programmet
    elif valg == "s":
        break
    valg = input("Skriv i for å legge til tekst, u for å skrive ut listen, eller s for å avslutte: ")






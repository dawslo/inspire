# Oppgave 15 - Regnefunksjoner

# 1) Skriv en funksjon addisjon som har to parametere. Funksjonen skal returnere summen av disse. Skriv en kodelinje som kaller på addisjon med heltallsargumenter du velger selv, og skriv ut resultatet.
def addisjon(tall1, tall2):
    return tall1 + tall2

# 2) Skriv tilsvarende funksjoner for subtraksjon, der du trekker det andre parameteren fra det første, og divisjon, der du deler den første parameteren på det andre.
def subtraksjon(tall1, tall2):
    return tall1 - tall2

def divisjon(tall1, tall2):
    return tall1 / tall2

# 3) Lag en funksjon tommerTilCm med ett parameter antallTommer. Deretter skal funksjonen returnere hvor mange centimeter antallTommer tilsvarer. For å regne om fra tommer til centimeter kan du gange antallTommer med 2.54. Test funksjonen din.
def tommerTilCm(antallTommer):
    return antallTommer * 2.54

#4) Lag en funksjon skrivBeregninger. Den skal ikke ta imot noen argumenter, men i stedet bruke input for å hente inn verdier fra bruker til kall på funksjonene du skrev over. Ta høyde for at brukeren kan skrive inn flyttall. 
def skrivBeregninger():
    # 4a) Først skal prosedyren hente inn to tall fra bruker. Disse tallene skal brukes som argumenter i kall på addisjon, subtraksjon og divisjon. Hver av disse funksjonene skal kalles og resultatet skrives ut til terminal.
    tall1 = float(input("Skriv inn et tall: "))
    tall2 = float(input("Skriv inn et tall til: "))
    print("Summen av tallene er", addisjon(tall1, tall2))
    print("Differansen mellom tallene er", subtraksjon(tall1, tall2))
    print("Kvotienten mellom tallene er", divisjon(tall1, tall2))
    # 4b) Deretter skal prosedyren hente inn et nytt tall som skal konverteres fra tommer til centimeter. Også dette resultatet skal skrives ut.
    tommer = input("Skriv inn et tall i tommer: ")
    print(tommer, "tommer er", tommerTilCm(float(tommer)), "centimeter")

# 5) Test skrivBeregninger.
skrivBeregninger()


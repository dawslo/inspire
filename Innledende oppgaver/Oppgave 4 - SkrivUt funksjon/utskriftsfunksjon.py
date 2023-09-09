# Oppgave 4: Skriv ut funksjon

# 4.1)	Lag et program som kommuniserer med brukeren slik at det tar imot et navn og et bosted fra terminalen, og skriver ut en melding.
navn = input("Skriv inn navn: ")
bosted = input("Skriv inn bosted: ")
print("\nHei, " + navn + "! Du er fra " + bosted + ".")

# 4.2) Flytt koden som leser inn informasjon og skriver ut en hilsen til en egen funksjon.
# Kall denne funksjonen 3 ganger slik at du får lest inn og skrevet ut informasjon om 3 personer.
def hilsen():
    navn = input("Skriv inn navn: ")
    bosted = input("Skriv inn bosted: ")
    print("\nHei, " + navn + "! Du er fra " + bosted + ".\n")

for i in range(3):
    hilsen()

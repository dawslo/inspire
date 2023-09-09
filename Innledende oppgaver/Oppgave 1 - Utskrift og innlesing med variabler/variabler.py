# Oppgave 1: Utskrift og innlesing med variabler
# 1. Lag en fil ved navn variabler.

# 2. Skriv et program i denne filen som skriver ut ”Hallo Verden!” til terminalen.
print("Hallo Verden!")

# 3. Endre programmet slik at du ber brukeren om å oppgi et navn i form av en tekststreng ved hjelp av funksjonen input(),
# og lagre denne verdien i en variabel navn. Skriv så ut “Hei “ og variabelen navn.
navn = input("Skriv inn navn: ")

print("Hei", navn)

# 4. Utvid programmet ditt med to variabler. Du kan velge variabelnavn selv, men gi begge variablene heltallsverdier. Skriv ut variablene på hver sin linje.
tall1 = 5
tall2 = 10
print(tall1)
print(tall2)

# 5. Beregne differansen av de to variablene (den første minus den andre) og legg resultatet inn i en ny variabel. 
# Skriv ut “Differanse:” etterfulgt av denne tredje variabelen. Du skal sjekke at begge tallene er heltall, og koden skal lage unntak hvis de ikke er det.
try:
    differanse = tall1 - tall2
    print("Differanse:", differanse)
except TypeError:
    print("En av variablene er ikke et heltall!")

# 6. Be bruker om å oppgi et nytt navn, og legg svaret i en ny variabel.
# Lag nok en variabel ved navn sammen, og gi den verdien av det første navnet etterfulgt av det andre navnet. Skriv ut sammen på en ny linje.

navn2 = input("Skriv inn et nytt navn: ")
sammen = navn + navn2
print(sammen)

# 7. Du skal nå endre verdien av variabelen sammen. Dette skal du gjøre ved å slå sammen de to navnene som i forrige deloppgave,
# men denne gangen skal du legge til “og” med et mellomrom på hver side mellom dem. For eksempel: Dersom sammen først hadde verdien “OlaKari!” skal den nå ha verdien “Ola og Kari”.  
# Viktig: Du skal utvide programmet ditt ved å endre verdien av variabelen sammen på en ny linje, ikke endre linjen der du først definerte variabelen.

sammen = navn + " og " + navn2
print(sammen)












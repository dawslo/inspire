
# 1.Skriv en funksjon innlesing, med et parameter filnavn. Denne funksjonen skal lese inn en fil ved hjelp av filnavn og legge alle linjene i filen inn i en ordbok,
# der den ansattes navn blir nøkkelverdien og antallet salg blir innholdsverdien (husk å konvertere innholdsverdien til et heltall). 
# Funksjonen skal deretter returnere ordboken.
def innlesing (filnavn):
    with open(filnavn, "r") as fil:
        return {line.split()[0]: int(line.split()[1]) for line in fil}
    
#2.	Lag en prosedyre maanedensSalgsperson som tar imot en ordbok, går gjennom denne og skriver ut navn og antall salg for den personen som solgte mest den måneden.
def maanedensSalgsperson(ordbok):
    maanedensSalgsperson = max(ordbok, key=ordbok.get)
    print(f"Månedens salgsperson er {maanedensSalgsperson} med {ordbok[maanedensSalgsperson]} salg.")

# 3.	Skriv en funksjon totaltAntallSalg som tar imot en ordbok og returnerer summen av innholdsverdiene i ordboken.
def totaltAntallSalg(ordbok):
    return sum(ordbok.values())

#4.	Lag en funksjon gjennomsnittSalg som tar imot en ordbok og returnerer gjennomsnittet av verdiene dens.
def gjennomsnittSalg(ordbok):
    return totaltAntallSalg(ordbok) / len(ordbok)

# 5. Til slutt skal du skrive en prosedyre hovedprogram(). Inne i hovedprogram skal du skrive ut den faktiske statistikken. 
# Bruk funksjonene og prosedyrene du har laget, og skriv i tillegg ut antall selgere som ble lest inn. Filen du skal bruke for å teste programmet ditt er salgstall.txt. 
# Denne txt.-filen skal levers sammen med resten av filene.
def hovedprogram():
    ordbok = innlesing(r"C:\Users\dawid\Innledende oppgaver1\Oppgave 18 - Salgsstatistikk\salgstall.txt")
    maanedensSalgsperson(ordbok)
    print(f"Aktive selgere denne maaneden: {len(ordbok)}")
    print(f"Totalt antall salg: {totaltAntallSalg(ordbok)}")
    print(f"Gjennomsnittlig antall salg per salgsperson: {gjennomsnittSalg(ordbok):.2f}")

hovedprogram()
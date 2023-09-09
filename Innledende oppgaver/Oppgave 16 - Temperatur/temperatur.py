#Oppgave 16: Temperatur
# 1. Les inn temperaturer fra fil
def les_temperatur_fra_fil(filnavn):
    with open(filnavn, "r") as fil:
        return [int(line.strip()) for line in fil]

# 2. Beregn gjennomsnittstemperaturen
def beregn_gjennomsnitt(temp_liste):
    total = 0
    for temp in temp_liste:
        total += temp
    return total / len(temp_liste)

# 3. Skriv ut gjennomsnittstemperaturen
temperatur_liste = les_temperatur_fra_fil(r"C:\Users\dawid\Innledende oppgaver1\Oppgave 16 - Temperatur\temperatur.txt")
gjennomsnitt = beregn_gjennomsnitt(temperatur_liste)
print(f"Gjennomsnittstemperaturen for året er: {gjennomsnitt:.2f}°C")








    


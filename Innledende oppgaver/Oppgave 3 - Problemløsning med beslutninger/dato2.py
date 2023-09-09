# Oppgave 3: Problemløsning med beslutninger (Frivillig)
# Frivillig: Skriv et nytt program i filen dato2 som gjør det samme som i punkt 2, men der brukeren skal skrive hver dato som ett heltall i stedet for to.
# Gi brukeren eksempel på hvordan datoen bør skrives for å sikre at sammenligningen i programmet ditt kan gjøres enklere enn i punkt 2.


# Melder bruker om å skrive inn dato som MMDD
print("Skriv inn datoen som MMDD \nEksempel: 4 Februar = 0204")

# Leser inn datoer
dato1 = int(input("Skriv inn første dato: "))
dato2 = int(input("Skriv inn andre dato: "))

# Sjekker rekkefølge, og skriver ut resultat
if dato1 < dato2:
    print("Riktig rekkefølge!")
elif dato1 > dato2:
    print("Feil rekkefølge!")
else:
    print("Samme dato!")








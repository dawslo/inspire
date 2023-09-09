#Oppgave 2: Beslutninger
#1.	Lag en fil med navnet beslutninger.

#2.	Skriv et program som ber brukeren om å svare “ja” eller “nei” på om de kunne tenke seg en brus. Lagre svaret i en variabel.
svar = input("Kunne du har tenkt deg en brus? (ja/nei): ")

#3.	Skriv en if-sjekk som tester hva brukeren har skrevet inn:
if svar.lower() == "ja":
    # a. Hvis brukeren har svart “ja” skal programmet skrive ut “Her har du en brus!”
    print("Her har du en brus!")
elif svar.lower() == "nei":
    # b. Hvis brukeren har svart “nei” skal setningen “Den er grei.” skrives ut.
    print("Den er grei.")
else:
    # c. Hvis brukeren har svart noe helt annet skal programmet skrive ut “Det forstod jeg ikke helt.”
    print("Det forsto jeg ikke helt")


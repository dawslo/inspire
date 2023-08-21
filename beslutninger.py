# Ber brukeren svare ja eller nei
svar = input("Kunne du har tenkt deg en brus? (ja/nei): ")

# Sjekker brukerens svar
if svar.lower() == "ja":
    print("Her har du en brus!")
elif svar.lower() == "nei":
    print("Den er grei.")
else:
    print("Det forsto jeg ikke helt")


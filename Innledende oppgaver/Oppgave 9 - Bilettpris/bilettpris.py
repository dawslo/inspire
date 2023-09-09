# Oppgave 9 - Bilettpris
#1.	Lag en funksjon som skal inneholde variablene alder og navn
def billettpris():
    navn = input("Vennligst oppgi ditt navn: ")
    alder = int(input("Vennligst oppgi din alder: "))

    pris = 0

# 3. Sjekk alder og tilordne riktig billettp
    if alder < 17:
        pris = 30
    elif alder >= 17 and alder <= 63:
        pris = 50
    else:
        pris = 35

 # 4. Skrive ut billettprisen til brukeren
    print(f"Hei, {navn}! Din billettpris er {pris} kroner.")

billettpris()  

        


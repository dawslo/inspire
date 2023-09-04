# Tomme lister
destinations = []
clothes = []
departure = []

# Ber brukeren skrive inn reisemål
for x in range(5):
    askDest = input("Reisemål: ")
    destinations.append(askDest)
    
# Ber brukeren skrive inn klær    
for x in range(5):
    askClothes = input("Klær: ")
    clothes.append(askClothes)

# Ber brukeren skrive inn avgang   
for x in range(5):
    askDep = input("Avgang: ")
    departure.append(askDep)
    
# Lager en felles liste av mindre lister
travel_plan = [destinations, clothes, departure]

# Skriver ut felles-liste
for x in travel_plan:
    print(x)
   
# Ber brukeren velge en liste og elemt fra valgt liste
try:
    i1 = int(input(f"Velg en liste (mellom 0 og {len(travel_plan) -1}): "))
    i2 = int(input(f"Velg en element fra valgt liste (mellom 0 og {len(travel_plan[i1]) -1}): "))
    
    # Skriver ut innholdet hvis input er riktig
    if 0 <= i1 <len(travel_plan) and 0 <= i2 < len(travel_plan[i1]):
        print(travel_plan[i1][i2])
        
    # Melder om ugyldig input
    else:
        print("Ugyldig input!")
except:
    print("Ugyldig input!")


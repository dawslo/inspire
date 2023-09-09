# Ordbok med beboere og måltider

food_plan = {
    "Oskar Pettersen": ["brød", "egg", "pølser"],
    "Noah Hagen": ["grøt", "salat", "fisk"],
    "Leah Andersen": ["pannekaker", "suppe", "kylling"],
    "Emma Tveit": ["cereal", "sandwich", "lasagne"],
    "Liam Johansen": ["yoghurt", "wraps", "taco"]
}



def show_food_plan():
    # Skriver ut navnene på beboerne
    print("Beboere på sykehjemmet: ")
    for resident in food_plan:
        print(resident)
        
    # Spør brukeren om å skrive inn et navn
    
    chosen_resident_input = input("\nSkriv inn navnet på en beboer for å se deres matplan: ")
    
    # Sjekker om beboeren finnes i ordboken
    chosen_resident = None
    for resident in food_plan:
            #Dette gjør at sjekken ikke er følsom for om navnet skrives med store eller små bokstaver
            if resident.lower() == chosen_resident_input.lower():
                chosen_resident = resident
                break
        
    if chosen_resident:
        food = food_plan[chosen_resident]
        print(f"\nMatplan for {chosen_resident}")
        print(f"Frokost: {food[0]}")
        print(f"Lunsj: {food[1]}")
        print(f"Middag: {food[2]}")
    # Skriver ut melding om beboer ikke er registrert.
    else:
        print("\nBeboeren er ikke registrert")
        
# Tester fuknsjonen
show_food_plan()
    
        
    

# Python har innebygde funksjoner som sum(), min() og max(),
# ved å bruke de hadde vi ikke trengt å skrive for-løkker,
# men oppgaven ber om å lage dem så jeg valgte å følge instruksene.

def main():
    # Tom liste for lagrende tall
    num_list = []
    
    # Leser in tall fra brukeren til brukeren taster 0
    while True:
        try:
            num = float(input("Tast inn et tall (0 for å avslutte): "))
            if num == 0:
                break
            num_list.append(num)
        except ValueError:
            print("Tast inn et gyldig tall!")
    
    # Går gjennom lista og skriver ut hvert element    
    print("\nTallene du tastet inn er:")
    for x in num_list:
        print(x)
    
    # Beregner summen av tallene
    sumNum = 0
    for x in num_list:
         sumNum += x
    print(f"\nSummen av tallene: {sumNum}")
    
    # Finner det minste elementet i listen
    smallestNum = float('inf')
    for x in num_list:
        if x < smallestNum:
            smallestNum = x
    print(f"\nDet minste tallet er: {smallestNum}")
    
    
    # Finner det største elementet i listen
    biggestNum = float('-inf')
    for x in num_list:
        if x > biggestNum:
            biggestNum = x
    print(f"\nDet største tallet er: {biggestNum}")
        
if __name__ == "__main__":
    main()    

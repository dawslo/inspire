# Oppgave 3: Problemløsning med beslutninger
# 1) Lag en fil med navnet dato.py

# 2) Skriv et program som ber om og leser inn to datoer, angitt med heltall for dag og måned (to variable for hver dato).
dato1_dag = int(input("Skriv inn dag for første dato: "))
dato1_mnd = int(input("Skriv inn måned for første dato: "))
dato2_dag = int(input("Skriv inn dag for andre dato: "))
dato2_mnd = int(input("Skriv inn måned for andre dato: "))


# 3) Skriv en if-test som tester hvilken dato som kommer først i samme år.
# b) Hvis den siste datoen som skrives inn er en tidligere dato, skal programmet skrive ut “Feil rekkefølge!”.
# c) Om datoene er like skrives “Samme dato!” ut.
if dato1_mnd < dato2_mnd:
    
    print("Riktig rekkefølge!")
elif dato1_mnd > dato2_mnd:
    print("Feil rekkefølge!")
else:
    if dato1_dag < dato2_dag:
        print("Riktig rekkefølge!")
    elif dato1_dag > dato2_dag:
        print("Feil rekkefølge!")
    else:
        print("Samme dato!")

# 4) Frivillig oppgave finnes i samme mappe som denne filen og heter dato2.py
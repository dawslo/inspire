# Oppgave 19: Motorsykkel
# Deloppgave 5: Test programmet ditt

# 5. I denne deloppgaven skal du teste programmet ditt. Opprett en ny fil testMotorsykkel.py. 
# Øverst i filen skal du importere klassen Motorsykkel. 
# Deretter skal du skrive en prosedyre hovedprogram(), slik som i oppgave 1.


from motorsykkel import Motorsykkel

# 6. Inne i hovedprogram skal du opprette et objekt av klassen Motorsykkel med et merke, et registreringsnummer og en kilometerstand.
def hovedoppgave():
    sykkel1 = Motorsykkel("BMW", "AB12345", 0)
    sykkel2 = Motorsykkel("Honda", "CD67890", 0)
    sykkel3 = Motorsykkel("Suzuki", "EF13579", 0)

    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()

hovedoppgave()


    
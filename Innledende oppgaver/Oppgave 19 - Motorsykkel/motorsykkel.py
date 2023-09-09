# Oppgave 19: Motorsykkel

# 1. Skriv klassen Motorsykkel med en konstruktør (init-metode) som initierer de instansvariablene klassen trenger.
class Motorsykkel:
    def __init__(self, merke, regnr, km):
        self._merke = merke
        self._regnr = regnr
        self._km = km

    # 2. Skriv en metode kjor(self, km) som øker kilometerstanden med det gitte antall kilometer.
    def kjor(self, km):
        self._km += km

    # 3. Skriv en metode hentKilometerstand(self) som returnerer motorsykkelens totale kilometerstand.
    def hentKilometerstand(self):
        return self._km
    
    # 4. Skriv en metode skrivUt(self) som skriver ut merke, registreringsnummer og kilometerstand.
    def skrivUt(self):
        print(f"Merke: {self._merke}\nRegistreringsnummer: {self._regnr}\nKilometerstand: {self._km}")


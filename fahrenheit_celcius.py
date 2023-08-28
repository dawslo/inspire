# Variabel for temperatur i fahrenheit
fahrenheit = 100

# Skriver ut temperaturen i fahrenheit
print(f"Temperaturen i Fahrenheit: {fahrenheit}°F")

# Konverterer fra fahrenheit til celcius 
celcius = ((fahrenheit - 32) * 5/9)

# Skriver ut temperaturen i celcius
print(f"Temperaturen i Ceclius: {celcius:.2f}°C")


# Modifisert til å hente bruker input
fahrenheit = float(input("Vennligst skriv inn temperaturen i Fahrenheit: "))

# Konverterer fra fahrenheit til celcius 
celcius = ((fahrenheit - 32) * 5/9)

# Skriver ut resultatene igjen
print(f"Temperaturen in Fahrenheit: {fahrenheit}°F")
print(f"Temperaturen in Celcius: {celcius:.2f}°C")
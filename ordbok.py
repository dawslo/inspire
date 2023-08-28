# Lager en ordbok med varenavn og pris
goods = {
    "melk": 14.90,
    "brød": 24.90,
    "yoghurt": 12.90,
    "pizza": 39.90
}

# Skriver ut innholdet i ordboken
print(goods)

# Les inn 2 nye varer med navn og pris fra brukeren
for _ in range(2):
    product = input("Skriv inn navnet på varen: ")
    price = float(input(f"Skriv inn prisen for {product}: "))
    goods[product] = price
    
# Skriver ut oppdatert ordbok
print(goods)
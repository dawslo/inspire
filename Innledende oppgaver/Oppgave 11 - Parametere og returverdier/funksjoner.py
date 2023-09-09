# Simpel adderingsfunksjon
def adder(num1, num2):
    return num1 + num2

# Kaller på fuknsjonen to ganger og skriver ut summen
sum1 = adder(5, 10)
sum2 = adder(10, 20)

# Skriver ut resultatene
print(sum1)
print(sum2)

# Funksjonen teller forekomster av en bokstav i en tekststreng
def countLetters(userText, userLetter):
    return userText.count(userLetter)

# Ber brukeren om en tekststreng og en bokstav
text_input = input("Skriv inn en tekststreng: ")
letter_input = input("SKriv inn en bokstav: ")

#Bruker funksjonen til å telle antall forekomster (CASE-SENSITIVE)
sum_char = countLetters(text_input, letter_input)

# Skriver ut resultalene
print(f"Bokstaven {text_input} forekommer {sum_char} ganger i teksten '{text_input}'")
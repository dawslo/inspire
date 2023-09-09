# Lager en liste med 3 tall
num_list = [5, 10, 15]

# Legger til tallet 20 til lista
num_list.append(20)

#Printer ut første og andre element i lista
print(num_list[0], num_list[2])

# Legger sammen elementene fra lista i variablen summen
sum1 = sum(num_list)

# Legger sammen tallene og multipliserer
product = 1
for num in num_list:
    product *= num

# Legger sammen de to resultatene i en ny liste
sum1_product_list = [sum1, product]

# Lager en ny liste ved å slå sammen num_list og sum1_product_list
combo_list = num_list + sum1_product_list


# Sletter siste 2 elemtene fra den kombinerte lista
del combo_list[-2:]

# Skriver ut kombinert liste
print(combo_list)

# Lager en ny tom liste
name_list = []

# Ber brukeren skrive inn 4 navn
for i in range(4):
    name = input("Skriv inn et navn: ")
    name_list.append(name)

# If-sjekk for å se om my_name fins i name_list
my_name = "Dawid"
if my_name in name_list:
    print("Du husket meg riktig!")
else: 
    print("Glemte du meg?")


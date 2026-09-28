numerot = []

num = int(input("anna numerot listaan: "))

print(numerot)
summa = 0

while num != 0:
    numerot.append(num)
    num = int(input("Anna joku numero listaan"))

for numero in numerot:
    summa += numero
    print("Summa nyt: ", summa)

print("Lopullinen summa on: ", summma)
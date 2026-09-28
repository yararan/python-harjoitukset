nimet = ["Viivi", "Ahmen", "Pekka", "Olga", "Mary"]

nimet2 = ["Matti", "Teppo"]

nimet.extend(nimet2)
print(nimet)

nimet.sort()
print(nimet)

if "Matti" in nimet:
    print("Matin indeksi on",nimet.index("Matti"))
else:
    print("Mattia ei löytynyt")




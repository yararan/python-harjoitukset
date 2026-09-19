muunnos = input("muutetaan syöttämäsi senttimetreiksi, anna tuumat: ")
cm = (float(muunnos))
tuumat = (float(2.54))

while True:
    tulos = tuumat * cm
    print("Antamasi tuumamäärä senttimetreinä ", tulos)
    if tulos > 0:
        break

else:
    print("Antamasi luku on negatiivinen, muunto päättyy tähän")

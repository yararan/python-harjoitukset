#määritetään tunnus ja salasana, nämä ei toki saisi olla näkyvät
tunnus = input("maijankone")
salasana = input("salainensana")

#pyydetään käyttäjää antamaan tunnus ja salasana
print("Hei, anna tunnus ja salasana seuraavaksi")
tunnus = input("syötä tunnus: ")
salasana = input("syötä salasana: ")


#reaktiot, jos menee oikein tai ei mene oikein
if tunnus == "maijankone":
    if salasana == "salainensana":
        print("tervetuloa")
elif tunnus != "maijankone":
    if salasana != "salainensana":
        print("not gonna happen")
            





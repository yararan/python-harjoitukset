tunnus = input("maijankone")
salasana = input("salainensana")

print("Hei, anna tunnus ja salasana seuraavaksi")
tunnus = input("syötä tunnus: ")
salasana = input("syötä salasana: ")

if tunnus == "maijankone":
    if salasana == "salainensana":
        print("tervetuloa")
elif tunnus != "maijankone":
    if salasana != "salainensana":
        print("not gonna happen")




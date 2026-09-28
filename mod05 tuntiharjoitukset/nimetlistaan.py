nimet = []

nimi= input("Anna joku nimi: ")
while nimi != "":
    nimet.append(nimi)
    nimi = input("Anna joku nimi: ")

print(nimet)

print("tulostetaan nimet: ")
for n in nimet:
    print(f"tervehdys, {n}!")

print("Ohjelma loppui")


#tätä en ehtinyt loppuun, joten varmaan pielessä
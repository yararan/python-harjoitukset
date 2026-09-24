print("---------TERVETULOA LASKINOHJELMAAN----------")

while True:
    print("valitse mitä toimintoa haluat käyttää:")
    print("A: yhteenlasku, B: vähennyslasku, C: kertolasku, D: jakolasku, Q = Lopeta ohjelma")
    valinta = input("anna valinta ").upper()

    if valinta == "Q":
            print("Poistutaan")
            
    if valinta not in ("A","B","C","D","Q"):
         print("virheellinen valinta tässä kohtaa")
         break
         

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    
    if valinta == "A":
        print(f"Lukujen {a} ja {b} summa on {a+b}.")
    elif valinta == "B":
        print(f"Lukujen {a} ja {b} erotus on {a-b}.")
    elif valinta == "C":
        print(f"Lukujen {a} ja {b} tulo on {a*b}.")
    elif valinta == "D":
        print(f"Lukujen {a} ja {b} osamäärä on {a/b}.") 
            
print("Ohjelma päättynyt")

#keksi parempi kohta ilmoittaa virheellisestä valinnasta
#kommentoi koodi = mitä se tekee missäkin kohtaa?"
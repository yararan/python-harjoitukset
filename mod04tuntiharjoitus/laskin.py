##ensin tulostetaan ohjelman nimi
print("\n---------TERVETULOA LASKINOHJELMAAN----------")

#annetaan yksinkertainen toistorakenne ja kysytään mitä toimintoa käytetään
while True:
    #infotaan käyttäjälle miten ohjelma toimii print-tulosteilla
    print("\nvalitse mitä toimintoa haluat käyttää:")
    print("A: yhteenlasku\nB: vähennyslasku\nC: kertolasku\nD: jakolasku\nQ = Lopeta ohjelma\n")

    #kysytään käyttäjältä mitä laskutustoimintoa käytetään
    valinta = input("anna valinta ").upper()

#valintojen ehdot
    if valinta == "Q":
            print("Poistutaan")
#Virheelliseen valintaan reagointi            
    if valinta not in ("A","B","C","D","Q"):
         print("virheellinen valinta tässä kohtaa")
         break
         
#laskuosio
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
#kerrotaan, että ohjelma päättyy. Ohjelma tullut ulos while-loopista            
print("Ohjelma päättynyt")

#keksi parempi kohta ilmoittaa virheellisestä valinnasta
#kommentoi koodi = mitä se tekee missäkin kohtaa?"

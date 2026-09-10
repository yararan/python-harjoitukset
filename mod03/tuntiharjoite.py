nimi = input("Anna nimesi ")

if nimi == "Matti":
    print("seuraava, kiitos!")

else:
    annos = int(input("Montako annosta?"))
    annoshinta = float(annos) * 5.90
    print(f"kokonaishinta on {annoshinta:.2f}, euroa")
    print("seuraava, kiitos!")
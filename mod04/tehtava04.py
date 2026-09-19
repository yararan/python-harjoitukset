import random

arvottu = random.randint(0,10)
print("Tässä koneen arpoma luku ", arvottu)


while True:
    arvaus = int(input("Ihminen, arvaa koneen arpoma luku "))
    if arvottu == arvaus:
        print("Oikein")
    break
else:
    print("Kokeile vielä")
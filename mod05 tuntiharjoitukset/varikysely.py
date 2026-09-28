varit = ["sininen", "punainen", "keltainen", "petrooli"]

lempivari = input("Mikä on lempivärisi ")

if lempivari in varit:
    print("väri löytyy listalta")
else:
    print("ei löydy listalta")

for v in varit:
    print(v)


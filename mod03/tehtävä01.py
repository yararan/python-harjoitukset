kuha = float(input("Anna kuhan pituus? "))
if kuha >= 37:
    print ("Kaikki ok")
if kuha < 37:
    kasvutarve = (37 - kuha)
    print ("Laske kuha järveen")
    print ("Kuha on alamittainen, anna sen kasvaa vielä: ", kasvutarve,  "cm")

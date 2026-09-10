sukupuoli = input("Oletko nainen vai mies? ")
hemo = float(input("Mikä on hemoglobiini tasosi? "))
if sukupuoli == "nainen":
    if (hemo >= 117 and hemo <= 175):
        print ("Naisen normaali hemoglobiiniarvo")
if sukupuoli == "nainen":
    if (hemo < 117):
        print ("Naisen matala hemoglobiiniarvo")
if sukupuoli == "nainen":
    if (hemo > 175):
        print ("Naisen korkea hemoglobiiniarvo")

if sukupuoli == "mies":
    if (hemo >= 134 and hemo <= 195):
        print ("Miehen normaali hemoglobiiniarvo")
if sukupuoli == "mies":
    if (hemo < 134):
        print ("Miehen matala hemoglobiiniarvo")
if sukupuoli == "mies":
    if (hemo > 195):
        print ("Mies korkea hemoglobiiniarvo")


else:
    print ("En ota kantaa - sukupuoli määrittelemätön")
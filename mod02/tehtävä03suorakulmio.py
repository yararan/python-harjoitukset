suorakulmionkanta_str = input ("Anna suorakulmion kanta: ") 
suorakulmionkorkeus_str = input ("Anna suorakulmion korkeus: ")
suorakulmionkanta = float(suorakulmionkanta_str)
suorakulmionkorkeus = float(suorakulmionkorkeus_str)
suorakulmionpiiri = suorakulmionkanta + suorakulmionkanta + suorakulmionkorkeus + suorakulmionkorkeus
suorakulmionpinta_ala = suorakulmionkanta * suorakulmionkorkeus
print ("suorakulmionpiiri on ", suorakulmionpiiri)
print ("suorakulmionpinta-ala on ", suorakulmionpinta_ala)
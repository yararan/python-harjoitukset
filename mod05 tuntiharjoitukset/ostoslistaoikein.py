#jotenkin näin

ostoslista = ["maito", "voi", "juusto"]

while ostoslista:
    tuote = input("mitä ostit?")
    ostoslista.remove(tuote)
    print("jäljellä olevat tuotteet", ostoslista)

leiviskä = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

leiviskä_grammoina = leiviskä * 20 * 32 * 13.3
naula_grammoina = naula * 32 * 13.3
luoti_grammoina = luoti * 13.3

grammat = leiviskä_grammoina + naula_grammoina + luoti_grammoina

kilogrammat = grammat // 1000
grammat = grammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat} grammaa.")
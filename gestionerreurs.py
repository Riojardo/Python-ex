Age=input("quelle age as tu ?")

try:
	Age=int(Age)
except:
	print("Ton age gros malin !")
else:
	print("quelle effet cela fait d'avoir",Age," années ?")
finally:
	print("Bip bop programme terminé")

nombreX = 93
nombreY = input("choisir diviseur: ")

""    ""
try:
	nombreY = int(nombreY)
	print("résultat:{}".format(nombreX /nombreY))
except ZeroDivisionError:
	print("ERROR ZERO")
except ValueError:
	print("ERROR VALOR INVALID")

	""   ""
try:
	age=input("Quelle est ton age mon gars")
	age=int(age)

	if age < 18:
		raise ZeroDivisionError
except ZeroDivisionError:
		print("Dégage le mome !!!")

""  ""
try:
	age=input("quel age as tu ? ")
	age=int(age)

	assert age > 18
except AssertionError:
	print("Dégage le mome !!!")

	

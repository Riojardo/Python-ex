Age=input("quelle age as tu ?")
Age=int(Age)

try:
	Age=int(Age)
	print("quelle effet cela fait d'avoir",Age," années ?")
except:
	print("Ton age gros malin !")

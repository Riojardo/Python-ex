print("hello world")
print((233+322)*9)

blessure= "coupure"
nom="Jean-eude"
age= 78
print(blessure)
print(type(blessure))

print(f"Je m'appelle {nom},j'ai {age} et je me suis fait une {blessure}")

"""
liste
"""
blessure= ["coupures","fractures","lésions","hématomes"]

print(blessure[0])
print(blessure[1])
blessure[-1]
blessure[3]

premier_type=blessure[0]
print(premier_type)
print(blessure[-1])

print(blessure)

("fractures") in blessure

fruit=["pomme","banane","orange"]
print(fruit)
fruit.append("kiwi")
print(fruit)
fruit.remove("orange")
print(fruit)
fruit[1]="anana"
print(fruit)
len(fruit)
fruit.sort()
print(fruit)
print(fruit[1])

"""
Dictionaire
"""
MonDico ={"race_de_chien":"labrador","age":39,"date_de_debut":"01/31/04"}
print(MonDico["age"])		
MonDico['race_de_chien']

nouvelle_campagne={
	"editrice":"Maria",
	"nom_promo":"le travail rends libre"
}
print(nouvelle_campagne["editrice"])
nouvelle_campagne["date_de_debut"]="Jeudi en 8"
print(nouvelle_campagne)
nouvelle_campagne["editrice"]="stéphanie"
print(nouvelle_campagne["editrice"])
del MonDico["race_de_chien"]
print(MonDico)
print("age" in MonDico)
print(nouvelle_campagne["nom_promo"])

"""
Condition
"""
sunny = 0
snow = 0
if sunny and snow:
	print("y a du soleil et de la neige créfieu ")
elif sunny or snow:
	print("je suis dehors en tout cas")
elif sunny and not snow:
	print("ilfait bon  c'est sur")
elif snow and not sunny:
	print("faisons un bonhomme de neige")
else:
	print("bon ben je reste chez moi")

nb_de_siege=30
nb_de_siege=int(nb_de_siege)

match nb_de_siege:
	case nb_de_siege = 30 :
		print("c'est complet")
	case nb_de_siege < 30 :
		print("il reste des place")
	case nb_de_siege > 30 :
		print("il faudras rembourser des tickets")


nombre_a_gauche=input("entrez nombre x :")
nombre_a_droite=input("entre nombre y :")
liste_operation =["+","-","/","*"]
operation=input("choisissez l'operation a effectuer :")
resultat= 0



print(nombre_a_gauche.isnumeric())
print(nombre_a_droite.isnumeric())
"""
if not nombre_a_droite.isnumeric() or not nombre_a_gauche.isnumeric():
	print("Erreur: les deux nombres doivent être des nombres entiers")
else:
	nombre_a_gauche= int(nombre_a_gauche)
	nombre_a_droite= int(nombre_a_droite)
	match operation:
		case "+":
			resultat = nombre_a_gauche + nombre_a_droite
			print(resultat)
		case "-":
			resultat = nombre_a_gauche - nombre_a_droite
			print(resultat)
		case "/":
			resultat = nombre_a_gauche / nombre_a_droite
			print(resultat)
		case "*":
			resultat = nombre_a_gauche * nombre_a_droite
			print(resultat)
"""
"""

nouvelle exemple
"""
def calculation(v1,v2,op):
	if not v2.isnumeric() or not v1.isnumeric():
		return("Erreur: les deux nombres doivent être des nombres entiers")
	if not operation in liste_operation:
		return("operateur invalide")
	v1= int(v1)
	v2= int(v2)
	if operation=="/" and v2==0:
		return("Division par zero invalide")
	match operation:
		case "+":
			return(v1 + v2)
		case "-":
			return(v1 - v2)
		case "/":
			return(v1 / v2)
		case "*":
			return(v1 * v2)
try:


	resultat=calculation(nombre_a_gauche,nombre_a_droite,operation)
	print(resultat)
except Error as e: 
	print(e)

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

	



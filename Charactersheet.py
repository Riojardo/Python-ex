listerace = ["human","elf","nain"]
listeclasse=["guerrier","mage","roublard","pretre"]
listegenre=["M","F","autre(s)"]

print(listerace)

race=0
while race != 1:
	race_joueur=input("Choisissez la race de votre personage parmis la liste ci-dessus: ")
	if not race_joueur in listerace:
		print("Race invalide")
		continue		
	else:	
		race =+ 1
		
print(listeclasse)

classe=0
while classe != 1:
	classe_joueur=input("Choisissez votre classe de personage parmis la liste ci-dessus: ")
	if not classe_joueur in listeclasse:
		print("Classe invalide")	
		continue		
	else:
		classe=+1
		
genre=0
while genre != 1:
	sex_joueur=input("Choissisez votre genre (M,F,autre(s)): ")
	if not sex_joueur in listegenre:
		print("veuillez réessayer")
		continue
	else:
			genre =+1
		
		
prenom_joueur=input("Donnez un prénom a votre personnage :")
F_nom_joueur=input("Donnez un nom de famille a votre caractère :")
nom_personnage=prenom_joueur +" "+F_nom_joueur
print("Votre personnage s'appelle :",nom_personnage)

STR=0
DEX=0
CON=0
INT=0
WIS=0
CHA=0

import random


def dice_rolls ():
	ability= [random.randint(1,6) for _ in range(4)]

	ability.sort(reverse=True)
	
	return sum(ability[:3]) 


abilities=[dice_rolls () for _ in range (6)]
abilities=sorted(abilities)

print("valeur des lancés obtenus :", abilities)


STR = int(STR)
DEX = int(INT)
CON = int(CON)
INT = int(INT)
WIS = int(WIS)
CHA = int(CHA)

if race_joueur == "human":
	abilities[5] += 1 
	abilities[4] += 1
elif race_joueur =="elf":
	DEX += 2
	INT += 1
elif race_joueur =="nain":
	CON += 2
	STR += 1


if classe_joueur == "guerrier":
	print("STR :",STR + abilities[5],"DEX :",DEX + abilities[3],"CON :",CON + abilities[4],"INT :",INT + abilities[0],"WIS :",WIS + abilities[2],"CHA :",CHA + abilities[1])
elif classe_joueur == "mage":
	print("STR :",STR + abilities[0],"DEX :",DEX + abilities[2],"CON :",CON + abilities[4],"INT :",INT + abilities[5],"WIS :",WIS + abilities[3],"CHA :",CHA + abilities[1])
elif classe_joueur == "roublard":
	print("STR :",STR + abilities[0],"DEX :",DEX + abilities[5],"CON :",CON + abilities[3],"INT :",INT + abilities[4],"WIS :",WIS + abilities[2],"CHA :",CHA + abilities[1])
elif classe_joueur == "pretre":
	print("STR :",STR + abilities[3],"DEX :",DEX + abilities[2],"CON :",CON + abilities[4],"INT :",INT + abilities[0],"WIS :",WIS + abilities[5],"CHA :",CHA + abilities[1])



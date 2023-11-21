listerace = ["human","elf","nain"]
listeclasse=["guerrier","mage","roublard","pretre"]
listegenre=["M","F"]

prenom_joueur=input("Donnez un prénom a votre personnage :")
F_nom_joueur=imput("Donnez un nom de famille a votre caractère :")
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

print("valeur obtenue :", abilities)

abilities_joueur={'STR':0,'DEX':0,'CON':0,'INT':0,'WIS':0,'CHA':0}

match classe:
	case "guerrier":
		abilities_joueur['STR'] = abilities[5]
		abilities_joueur['DEX'] = abilities[3]
		abilities_joueur['CON'] = abilities[4]
		abilities_joueur['INT'] = abilities[0]
		abilities_joueur['WIS'] = abilities[2]
		abilities_joueur['CHA'] = abilities[1]
	case "mage":
		abilities_joueur['STR'] = abilities[0]
		abilities_joueur['DEX'] = abilities[2]
		abilities_joueur['CON'] = abilities[4]
		abilities_joueur['INT'] = abilities[5]
		abilities_joueur['WIS'] = abilities[3]
		abilities_joueur['CHA'] = abilities[1]
	case "pretre":
		abilities_joueur['STR'] = abilities[3]
		abilities_joueur['DEX'] = abilities[2]
		abilities_joueur['CON'] = abilities[4]
		abilities_joueur['INT'] = abilities[0]
		abilities_joueur['WIS'] = abilities[5]
		abilities_joueur['CHA'] = abilities[1]
	case "roublard":
		abilities_joueur['STR'] = abilities[0]
		abilities_joueur['DEX'] = abilities[5]
		abilities_joueur['CON'] = abilities[3]
		abilities_joueur['INT'] = abilities[4]
		abilities_joueur['WIS'] = abilities[2]
		abilities_joueur['CHA'] = abilities[1]


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

if clase_joueur == "guerrier":
	print("STR :",STR + abilities[5],"DEX :",DEX + abilities[3],"CON :",CON + abilities[4],"INT :",INT + abilities[0],"WIS :",WIS + abilities[2],"CHA :",CHA + abilities[1])
elif clase_joueur == "mage":
	print("STR :",STR + abilities[0],"DEX :",DEX + abilities[2],"CON :",CON + abilities[4],"INT :",INT + abilities[5],"WIS :",WIS + abilities[3],"CHA :",CHA + abilities[1])
elif clase_joueur == "roublard":
	print("STR :",STR + abilities[0],"DEX :",DEX + abilities[5],"CON :",CON + abilities[3],"INT :",INT + abilities[4],"WIS :",WIS + abilities[2],"CHA :",CHA + abilities[1])
elif clase_joueur == "pretre":
	print("STR :",STR + abilities[3],"DEX :",DEX + abilities[2],"CON :",CON + abilities[4],"INT :",INT + abilities[0],"WIS :",WIS + abilities[5],"CHA :",CHA + abilities[1])



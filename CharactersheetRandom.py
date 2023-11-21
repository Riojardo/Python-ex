import random

race = ["human","elf","nain"]
classe=["guerrier","mage","roublard","pretre"]
genre=["M","F"]
name_humain_M=["Bob","André","Gerard","Jean-Philibert","Gonzague"]
name_elf_M=["Varis","Elrond","Glorfindel"]
name_nain_M=["Theurik","Gothrek","Gimli"]
name_humain_F=["Cindy","vanessa","Kimberley","Khalan","Myriam"]
name_elf_F=["Sosiel","Elendil","Euridyce"]
name_nain_F=["Gertrude","Gothrekia","Maurice","Fafnir"]
fam_name_humain=["Smith","LeTellier","Dupuis","van Richtofen"]
fam_name_elf=["Esoriel","Azratil","Kolean","Ashara"]
fam_name_nain=["Fer-Ecu","Poing d'Acier","Fier de la Hache","Barberouille"]

STR=0
DEX=0
CON=0
INT=0
WIS=0
CHA=0

race_joueur=random.choice(race)
print("Votre race est :",race_joueur)

clase_joueur=random.choice(classe)
print("Votre classe est :",clase_joueur)

genre_joueur=random.choice(genre)
print("Sexe du joueur :",genre_joueur)

if race_joueur == "human" and genre_joueur == "M":
	name_joueur=(random.choice(name_humain_M) +" "+ random.choice(fam_name_humain))
	print("Votre personnage s'appelle :",name_joueur)

if race_joueur == "human" and genre_joueur == "F":
	name_joueur=(random.choice(name_humain_F) +" "+ random.choice(fam_name_humain))
	print("Votre personnage s'appelle :",name_joueur)

if race_joueur == "elf" and genre_joueur == "M":
	name_joueur=(random.choice(name_elf_M) +" "+ random.choice(fam_name_elf))
	print("Votre personnage s'appelle :",name_joueur)

if race_joueur == "elf" and genre_joueur == "F":
	name_joueur=(random.choice(name_elf_F) +" "+ random.choice(fam_name_elf))
	print("Votre personnage s'appelle :",name_joueur)

if race_joueur == "nain" and genre_joueur == "M":
	name_joueur=(random.choice(name_nain_M) +" "+ random.choice(fam_name_nain))
	print("Votre personnage s'appelle :",name_joueur)

if race_joueur == "nain" and genre_joueur == "F":
	name_joueur=(random.choice(name_nain_F) +" "+ random.choice(fam_name_nain))
	print("Votre personnage s'appelle :",name_joueur)


def dice_rolls ():
	ability= [random.randint(1,6) for _ in range(4)]

	ability.sort(reverse=True)
	
	return sum(ability[:3]) 


abilities=[dice_rolls () for _ in range (6)]
abilities=sorted(abilities)

print("valeur obtenue :", abilities)

abilities_joueur={'STR':0,'DEX':0,'CON':0,'INT':0,'WIS':0,'CHA':0}

STR = int(STR)
DEX = int(DEX)
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
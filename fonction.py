def compter_jusqu_a_cinque():
	variable=1
	variable=int(variable)
	while variable<=5:
		print(variable)
		variable += 1

compter_jusqu_a_cinque()

def Declaration(nom,metier,ans,salutation):
	print("{}({})(age:{}):{}".format(nom,metier,ans,salutation))

Declaration("bobby","charcutier","23","what's uuuuuup ?!")
Declaration(salutation="yo",ans="17",metier="soudeur",nom="charle")

def organes_manquants(*list_organes):
	for organes in list_organes:
		print(organes)

organes_manquants("coeur","poumons","foie","cerveau","intestins")

def exposant2(nombre):
	return nombre*nombre

print(exposant2(3))


salaire_annuel=input("saisisez votre salaire annuel :")
nb_heure=input("saisisez le nombre d'heure par semaine :")

def salaire_mensensuel (salaire_annuel):
	resultat_mensuel = salaire_annuel/12
	return resultat_mensuel

def salaire_hebdomadaire(salaire_mensensuel):
		resultat_hebdomadaire = salaire_mensensuel/4
		return resultat_hebdomadaire


def salaire_horraire(salaire_hebdomadaire,nb_heure):
	resultat_horraire = salaire_hebdomadaire/nb_heure
	return resultat_horraire


print(salaire_horraire(salaire_hebdomadaire,nb_heure))






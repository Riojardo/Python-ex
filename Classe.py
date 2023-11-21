class UnHumain:

	"""
	Classe des ettre humain
	"""
	def __init__(self,C_prenom="toto",C_age=1):
		print("creation d'un humain ")
		self.prenom = C_prenom
		self.age = C_age
		

print("Lancement de programme")


h1=UnHumain("Jean-Eude",16)
print("Prénom de h1 :{} ".format(h1.prenom))
print("Age de h1 :{} ".format(h1.age))
h2=UnHumain("Victore")
print("Prénom de h2 :{} ".format(h2.prenom))
print("Age de h2 :{} ".format(h2.age))

class Charcuterie(object):
	"""docstring for Charcuterie"""
	def __init__(self, c_salée=True,c_fumée=False,c_poid=1):
	
		self.salée= c_salée
		self.fumée=c_fumée
		self.poid=c_poid

viande1=(False,False,10)
print("salée ?: {}".format(viande1.salée))
print("fumée ?:{}".format(viande1.fumée))
print("poid en KG:{}".format(voande1.poid))
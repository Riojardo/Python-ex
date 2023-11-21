class Chanteur:
	"""docstring for ClassName"""
	def __init__(self, nom,style):
		self.nom=nom
		self.style=style

	def chanter(self,chanson):
		print("{} a chanté :{}".format(self.nom,chanson))

Chanteur1=Chanteur("Claude","rock")
print("le chanteur {}".format(Chanteur1.nom))
print("qui fait du {}".format(Chanteur1.style))		

Chanteur1.chanter ("lalalala")
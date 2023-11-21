valeur=1
valeur=int(valeur)

while valeur<=100:
	print(valeur,"killometre a pied; ca use ;ca use")
	valeur +=1

print("ca use les souliers")

activation = True

while activation:
	choixmenu = input(">:")
	if choixmenu == "again":
		print("on continue donc")
	elif choixmenu == "ca_vas ?":
		print("Ben écoute ca vas pas mal")
	elif choixmenu == "Bonjour":
		print("Ouaip;bien le bonjour :)")
	elif choixmenu =="quitter":
		activation= False
	else:
		print("WTF!")

print("Merci et a bientot!")

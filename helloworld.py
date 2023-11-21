print("hello, world")
#coding:utf-8
print("bonjout tot le monde")

nb_entier=(input("veuillez créer une suite de nombre "))

liste=nb_entier.split()
int_list=list(map(int,liste))
print(int_list)
n=(len(int_list))
print(n)

total = 0

for ele in int_list:
	total = total + ele
print("somme de tous les élement" , total)

moyenne = total/n
print(moyenne)
	
nb_supmoy = 0
for ele in int_list:
	if ele > moyenne:
		nb_supmoy += 1
	
print(nb_supmoy)

nb_elementpair=0
compteur=0

while compteur < n:
	
	if  int_list[compteur]%2==0:
		nb_elementpair+=1
	compteur += 1
	
print(nb_elementpair)
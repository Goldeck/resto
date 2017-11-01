with open("resto.txt","r") as file:
	readfile=file.readlines()

print(readfile)
print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")

def recupetxt(line):
	listeelem=line.strip().split(",")
	nom=listeelem[0]
	num=listeelem[1]
	photo=listeelem[2]

	return transformehtml(nom,num,photo)




def transformehtml(nom,num,photo):

	monblock='''<div>
	<img src="%s ">
	<p>le nom du resto : <a href=/formulaire"page2.htm">%s</a> </p>
	<p>le num du resto : %s</p>
</div>''' % (photo,nom,num)

	return monblock

# for line in readfile:
# 	print(recupetxt(line))




def combinemesboucles(readfile):
	boutcoller=""
	for line in readfile:
		boutdecode=recupetxt(line)
		boutcoller+=boutdecode
	return boutcoller

# print(combinemesboucles(readfile))



def verifresto(readfile):
	listnom=[]
	for line in readfile:
		listeelem=line.strip().split(",")
		nom=listeelem[0]
		listnom+=[nom]
		
	return listnom


def verifi(nomr):
	listnom=verifresto(readfile)
	
	if nomr in listnom:
		return "le resto existe"
	else:
		return "le resto n'existe pas"



print(verifresto(readfile))
print(verifi("Quick"))

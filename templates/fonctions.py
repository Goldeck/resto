def tanformlinehtml(line):
	listeelem=line.strip().split(",")
	nom=listeelem[0]
	num=listeelem[1]
	photo=listeelem[2]

	return transformehtml(nom,num,photo)


def transformehtml(nom,num,photo):

	monblock='''<div>
	<img src="%s ">
	<p>le nom du resto : <a href="/%s">%s</a> </p>
	<p>le num du resto : %s</p>
	</div>''' % (photo,nom,nom,num)

	return monblock


def combinemesboucles(readfile):
	boutcoller=""
	for line in readfile:
		boutdecode=tanformlinehtml(line)
		boutcoller+=boutdecode
	return boutcoller

def get_resto_list(readfile):
	listnom=[]
	for line in readfile:
		listeelem=line.strip().split(",")
		nom=listeelem[0]
		listnom+=[nom]
		
	return listnom


def get_resto_html(nomr):
	with open("resto.txt","r") as file:
		readfile=file.readlines()

	listnom=get_resto_list(readfile)
	app.logger.info(listnom)
	if nomr in listnom:
		dependances = {
			"menu" : {
				"versios" : [1.1,2.1],

			}
		}


		with open("Donnees/"+nomr+".txt","r") as file:
			menu=str(file.readlines())

		page=render_template("restaurant.html",listeplat=menu , resto=nomr)

		return page
	else:
		return "le resto n'existe pas"
# coding: utf-8
from __future__ import print_function
from flask import Flask, render_template, request, redirect, url_for
import sys

# !/usr/bin/python
 
import cgi

app = Flask(__name__)

with open("resto.txt","r") as file:
	readfile=file.readlines()


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
		


		formulaire =  '''
	<form method="POST" action="/'''+nomr+'''">
	<p>Vos plats</p>
	<p>
	<label for="plat">Votre plat :</label>
	<input type="text" name="plat" id="plat" placeholder="Ex : kebab" size="30" maxlength="10" />
	</p>
	<p>
	<label for="description">description du plat :</label>
	<input type="text" name="description" id="description" size="30"/>
	</p>
	<p>
	<label for="prix">prix du plat :</label>
	<input type="text" name="prix" id="prix" size="30" />
	</p>
	<p>
	<label for="photo">photo du plat  :</label>
	<input type="text" name="photo" id="photo" size="30" />
	</p>
	<input type="submit" value="Envoyer" />
	</form>
	'''

		with open("Donnees/"+nomr+".txt","r") as file:
			meunu=str(file.readlines())


		return meunu+formulaire
	else:
		return "le resto n'existe pas"


@app.route("/<name>")
def meunuresto(name):


	# plat =  str(request.form['plat'])
	# description =  str(request.form['description'])
	# prix =  str(request.form['prix'])
	# photo =  str(request.form['photo'])

	# with open("Donnees/"+name+".txt","a") as file:
	# 	file.write(plat+ "," +description+","+prix+","+ photo+",\n")
	return verifi(name)


# @app.route("/<name>", methods=['GET'])
# def meunuresto(name):

# 	return verifi(name)

# @app.route("/<name>")
# def meunuresto(name):
# 	if name in meunu_resto:
# 		return "<html><body> <h1> VidÃ©os prÃ©fÃ©rÃ©es </h1> <p>  " + ",".join(meunu_resto[name]) + " </p> </body></html>"    
# 	else:
# 		return "<html><body> <h1> Create an account please </h1> <p>  you will like it. </p> </body></html>"    


@app.route("/resto", methods=['GET'])
def monindex():





	with open("resto.txt","r") as file:
		readfile=file.readlines()


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

	restoenre=combinemesboucles(readfile)

	

	formulaire =  '''
	<form method="POST" action="/resto">
	<p>Nom du resto</p>
	<p>
	<label for="nom">nom du resto :</label>
	<input type="text" name="nom" id="nom" size="30" maxlength="10" />
	</p>
	<p>
	<label for="description">numero de tel :</label>
	<input type="text" name="num" id="num" size="30"/>
	</p>
	<p>
	<label for="photo">photo du resto  :</label>
	<input type="text" name="photo" id="photo" size="30" />
	</p>
	<input type="submit" value="Envoyer" />
	</form>
	'''


	return restoenre+formulaire

@app.route("/resto", methods=['POST'])
def nouvellepage():
	import random
	formulaire =  '''
	rafréchisser la page pour verifier que le resto a bien ete enregistrer
	'''
	

	nom =  str(request.form['nom'])
	num =  str(request.form['num'])
	photo =  str(request.form['photo'])

	open("Donnees/"+nom+".txt", "a")

	with open("resto.txt","a") as file:
		file.write(nom+ "," +num+","+ photo+",\n")

	return image + formulaire + str(request.form['nom']) 


#flask templates













@app.route("/formulaire", methods=['GET'])
def monmenu():


	with open("liste.txt","r") as file:
		readfile=file.read()
	formulaire =  '''
	<form method="POST" action="/formulaire">
	<p>Vos plats</p>
	<p>
	<label for="plat">Votre plat :</label>
	<input type="text" name="plat" id="plat" placeholder="Ex : kebab" size="30" maxlength="10" />
	</p>
	<p>
	<label for="description">description du plat :</label>
	<input type="text" name="description" id="description" size="30"/>
	</p>
	<p>
	<label for="prix">prix du plat :</label>
	<input type="text" name="prix" id="prix" size="30" />
	</p>
	<p>
	<label for="photo">photo du plat  :</label>
	<input type="text" name="photo" id="photo" size="30" />
	</p>
	<input type="submit" value="Envoyer" />
	</form>
	'''


	return readfile+formulaire

@app.route("/formulaire", methods=['POST'])
def monmeunupost():
	import random
	titre = "<h1>" + str(random.randint(1,10)) + "</h1>"
	formulaire =  '''
	vous avez cliquer sur OKKKKK!
	'''
	

	plat =  str(request.form['plat'])
	description =  str(request.form['description'])
	prix =  str(request.form['prix'])
	photo =  str(request.form['photo'])

	with open("liste.txt","a") as file:
		file.write(plat+ "," +description+","+ prix+ ","+ photo+",\n")

	return titre + formulaire + str(request.form['prix']) 












if __name__ == "__main__":
    app.run(debug=True, port = 8000)
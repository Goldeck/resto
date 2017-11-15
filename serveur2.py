# coding: utf-8
#!/usr/bin/python
from __future__ import print_function
from flask import Flask, render_template, request, redirect, url_for
import sys

app = Flask(__name__)



def recupinforesto(line):
	listeelem=line.strip().split(",")
	nom=listeelem[0]
	num=listeelem[1]
	photo=listeelem[2]
	return affichageresto(nom,num,photo)

def recupinfoplat(line):
	listeelem=line.strip().split(",")
	nomplat=listeelem[0]
	description=listeelem[1]
	prix=listeelem[2]
	lienimage=listeelem[3]
	return affichageplat(nomplat,description,prix,lienimage)


def affichageresto(nom,num,photo):

	monblock='''<div>
	<img src="%s ">
	<p>le nom du resto : <a href="/%s">%s</a> </p>
	<p>le num du resto : %s</p>
	</div>''' % (photo,nom,nom,num)

	return monblock

def affichageplat(nomplat,description,prix,lienimage):
	affichageplat='''<div>
        <p>le nom du plat : %s</a> </p>
        <p>le desciption du plat : %s</p>
        <p>le prix du plat : %s</p>
        <img src="%s ">
    </div>'''% (nomplat,description,prix,lienimage)
	return affichageplat

def combinemesboucles(readfile):
	boutcoller=""
	for line in readfile:
		boutdecode=recupinforesto(line)
		boutcoller+=boutdecode
	return boutcoller


def combinemesbouclesplat(readfile):
	boutcoller=""
	for line in readfile:
		boutdecode=recupinfoplat(line)
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





		# affichageplat=affichageplat(nomplat,description,prix,lienimage)

		page=render_template("restaurant.html",listeplat=menu , resto=nomr)

		return page
	else:
		return "le resto n'existe pas"


@app.route("/<name>", methods=['POST'])
def meunuresto(name):


	plat =  str(request.form['plat'])
	description =  str(request.form['description'])
	prix =  str(request.form['prix'])
	photo =  str(request.form['photo'])

	with open("Donnees/"+name+".txt","a") as file:
		file.write(plat+ "," +description+","+prix+","+ photo+",\n")
	return get_resto_html(name)


@app.route("/<name>", methods=['GET'])
def meunuresto2(name):

	with open("Donnees/"+name+".txt","r") as file:
		readfile=file.readlines()




	platresto=combinemesbouclesplat(readfile)

	formulaire = render_template("formulaire_resto.html")


	return platresto+get_resto_html(name)


@app.route("/resto", methods=['POST'])
def nouvellepage():
	
	nom =  str(request.form['nom'])
	num =  str(request.form['num'])
	photo =  str(request.form['photo'])

	open("Donnees/"+nom+".txt", "a")

	with open("resto.txt","a") as file:
		file.write(nom+ "," +num+","+ photo+",\n")

	return redirect("/resto")


@app.route("/resto", methods=['GET'])
def monindex():

	with open("resto.txt","r") as file:
		readfile=file.readlines()




	restoenre=combinemesboucles(readfile)

	formulaire = render_template("formulaire_resto.html")

	return restoenre+formulaire




if __name__ == "__main__":
    app.run(debug=True, port = 8000)
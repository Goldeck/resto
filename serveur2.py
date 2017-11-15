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

	plat ={
		"nomplat" : listeelem[0],
		"description" : listeelem[1],
		"prix" : listeelem[2],
		"lienimage" : listeelem[3]
	}
	return plat


def affichageresto(nom,num,photo):

	monblock='''<div>
	<img src="%s ">
	<p>le nom du resto : <a href="/%s">%s</a> </p>
	<p>le num du resto : %s</p>
	</div>''' % (photo,nom,nom,num)

	return monblock



def combinemesboucles(readfile):
	boutcoller=""
	for line in readfile:
		boutdecode=recupinforesto(line)
		boutcoller+=boutdecode
	return boutcoller


def combinemesbouclesplat(readfile):
	plats=[]
	for line in readfile:
		plat=recupinfoplat(line)		
		plats.append(plat)

	return plats


def get_resto_list(readfile):
	listnom=[]
	for line in readfile:
		listeelem=line.strip().split(",")
		nom=listeelem[0]
		listnom+=[nom]
		
	return listnom


def restaurant_existe(nomr):
	with open("resto.txt","r") as file:
		readfile=file.readlines()

	listnom=get_resto_list(readfile)

	return nomr in listnom
	# la même chose
	# if nomr in listnom:
	# 	return True
	# else:
	# 	return False

def get_food_lines(name):
	with open("Donnees/"+name+".txt","r") as file:
		readfile=file.readlines()
	return readfile		


@app.route("/<name>", methods=['POST'])
def meunuresto(name):


	plat =  str(request.form['plat'])
	description =  str(request.form['description'])
	prix =  str(request.form['prix'])
	photo =  str(request.form['photo'])

	with open("Donnees/"+name+".txt","a") as file:
		file.write(plat+ "," +description+","+prix+","+ photo+",\n")
	return redirect("/" + name )




@app.route("/<name>", methods=['GET'])
def meunuresto2(name):	
	if restaurant_existe(name):
		
		readfile=get_food_lines(name)

		plats=combinemesbouclesplat(readfile)

		page= render_template("restaurant.html",plats=plats,resto=name)
		return page
	else :
		return "aucun restaurant de ce nom"




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
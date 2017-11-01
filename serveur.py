# coding: utf-8
from __future__ import print_function
from flask import Flask, render_template, request, redirect, url_for
import sys

# !/usr/bin/python
 
import cgi

app = Flask(__name__)


videos_preferees = {
    "titi" : ["squeezie", "cyprien"],
    "toto" : ["chicken_attack"]
}

# @app.route("/<name>")
# def zoeijrozie(name):
#     if name in videos_preferees:
#         return "<html><body> <h1> VidÃ©os prÃ©fÃ©rÃ©es </h1> <p>  " + ",".join(videos_preferees[name]) + " </p> </body></html>"    
#     else:
#         return "<html><body> <h1> Create an account please </h1> <p>  you will like it. </p> </body></html>"    




 





@app.route("/")
def afeeafzaf():
    return "index.html"

@app.route("/formulaire", methods=['GET'])
def monindex():


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
def nouvellepage():
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


#flask templates






# @app.route("/testMethod", methods=["POST", "GET"])
# def testMethod():
#     if request.method == "GET":
#         return "Tu as fait un GET"
#     elif request.method == "POST":
#         return "Tu as fait un POST"



# formulaire POST.


if __name__ == "__main__":
    app.run(debug=True, port = 8000)
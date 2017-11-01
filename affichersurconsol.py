# coding: utf-8
f=open("liste.txt",'r')

lines=f.readlines()
f.close()

# print(lines[1])


def affichage(line):
	# print(line)
	# print(line.strip().split(","))
	# for mot in line.split(","):
	# 	print(mot)
	mots=line.strip().split(",")
	print(mots[0].upper()
		+" ("+mots[2]+"€) : "+mots[1])


for line in lines:
	affichage(line)

# affichage(lines[0])
# affichage(lines[1])
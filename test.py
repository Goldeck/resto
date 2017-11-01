fruits = ["pomme", "banane", "ananas"]
print(fruits)
print(fruits[0])

i = 0
longueur = len(fruits)
print(longueur)

for i in [0,1,2]:
	fruit = fruits[i]
	print(fruit)

for fruit in fruits:
	print(fruit)

def plus(a, b):
	return a + b

def max(a, b):
	if a >= b:
		return a
	else:
		return b

print(max(123,1000))
print(plus(1,2))


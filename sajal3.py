import random

d = 0
p = 0

while True:
	r = input("press r to roll, q to quit : ")

	if r == 'r':
		d = random.randint(1,6)
		print("You got :",d)
		if d == 6:
			print("congratulations, you can play now.")
			break
		else:
			print("roll again, till you get 6.")

while True:
	r = input("press r to roll, q to quit : ")

	if r == 'r':
		d = random.randint(1,6)
		print("You got :",d)

		p = p+d
		if p > 100:
			p = p-d
			print("wait till you get", 100+p)

		print("Your new position is :",p)

		if p == 100:
			print("You won!")
			exit()
		if p == 8:
			p = 37
			print("Wow, a ladder. Go to ",p)
		if p == 3:
			p = 34
			print("Wow, a ladder. Go to ",p)
		if p == 40:
			p = 68
			print("Wow, a ladder. Go to ",p)
		if p == 52:
			p = 81
			print("Wow, a ladder. Go to ",p)
		if p == 76:
			p = 97
			print("oops, a snake. Go to ",p)
		if p == 25:
			p = 4
			print("oops, a snake. Go to ",p)
		if p == 38:
			p = 9
			print("oops, a snake. Go to ",p)
		if p == 65:
			p = 46
			print("oops, a snake. Go to ",p)
		if p == 89:
			p = 70
			print("oops, a snake. Go to ",p)
		if p == 93:
			p = 64
			print("oops, a snake. Go to ",p)
		if p == 11:
			p = 1
			print("oops, a snake. Go to ",p)
	
	
		elif r == 'q':
			print("Bye!")
			exit()




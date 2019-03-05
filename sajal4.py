import random

p = 0
d = 0
snl={8:37,13:34,38:9,11:2,28:4,40:68,52:81,76:97,65:46,93:64,89:70}

#Function to roll the dice
def rolldice():
	return random.randint(1,6)

#Get 1 or 6 on the dice to enter the game.
while True:
	r = input("press r to roll the dice, q to quit : ")
	if r == 'r':
		d = rolldice()
		print("You got",d)

		if d ==6 or d ==1:
			p = d
			print("congratulation, you're in the game!")
			print("You start on",p)
			break
		else:
			print("You need to get 6 or 1 to start. Try again.")
	elif r == 'q':
		exit()

while True:

	r = input("Press r to roll the dice, q to quit : ")

	if r == 'r':
		d = rolldice()
		print("You got",d)
		p = p + d

		if p == 100:
			print("Hurray! You won!")
			exit()

		if p > 100:
			p = p - d
			print("You need to get", 100-p,"to reach home.")
		print("Your new position is",p)

		if p in snl:
			if p <  snl[p]:
				print("Wow, you go a ladder.")
			else:
				print("oooops, you got bitten by a snake.")

			p = snl[p]
			print("move to ",p)
		elif r == 'q':
			exit()

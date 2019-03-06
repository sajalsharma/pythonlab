d=6

for i in range(6):
	r=input(" press r to roll q to quit")
	if r == 'r':
		if i%3 == 0:
			print("you got : ",d)
		elif i%3 == 1:
			print("you got : ",d/3)
		elif i%3 == 2:
			print("you got : ",d/2)



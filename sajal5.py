import random
l=["rock","paper","scissor"]
f=0
k=0
my = {'scissor':'s',
	'rock':'r',
	'paper':'p'}
while True:
	#take input from user
	print(my)
	u=input("if user chooses,press e to discontinue")
	#to exit
	if u=='n':
		print("Game over")
		print("comp score",k)
		print("user score",f)
		exit()
	#input from computer
	c=random.choice(l)
	print ("computer chooses ",c)

	#compare the user and computer choice
	if u == c:
		print("tie",my[u],"user have chooses",my[c],"comp has chooses")
		print("comp score",k)
		print("user score",f)
	elif u=="rock" and c=="paper":
		k=k+1
		print("comp wins",my[u],"user have chooses",my[c],"comp has chooses")
		print("comp score",k)
		print("user score",f)
	elif u == 'rock' and c =="scissor":
		f=f+1
		print("user wins",my[u],"user have chooses",my[c],"comp has chooses")
		print("comp score",k)
		print("user score",f)
	elif u=="paper" and c=="scissor":
		k=k+1
		print("comp wins",my[u],"user have chooses",my[c],"comp has chooses")
		print("comp score",k)
		print("user score",f)
	elif u=="paper" and c=="rock":
		f=f+1
		print("user wins",my[u],"user have chooses",my[c],"comp has chooses")
		print("comp score",k)
		print("user score",f)
	elif u=="scissor" and c=="paper":
		f=f+1
		print("user wins",my[u],"user have chooses",my[c],"comp has chooses")
		print("comp score",k)
		print("user score",f)
	elif u=="scissor" and c=="rock":
		k=k+1
		print("comp wins",my[u],"user have chooses",my[c],"comp has chooses")
		print("comp score",k)
		print("user score",f)

	



































def func1(k):
	print("hii",k)
func1("sajal")

def func(a,b,c):
	d=a+b+c
	print(d)
func(3,4,6)

#with default parameter
def func4(university="IITB"):
	print("I am in" + "\t"+ university)
func4("IITG")
func4("IITD")
func4()

#calling one function from other and return statement

def func5(a,b):
	print("hii other function") 
	c=a+b
	return c




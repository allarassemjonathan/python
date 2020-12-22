import math as mt
"""
we calculate delta = bsquare - 4ac
"""
def delta(a,b,c):
	return b*b-4*a*c

"""
we calculate the greater root if delta>0
"""
def xG(a,b,c):
	if(delta(a,b,c) > 0):
		x1 = (-b - mt.sqrt(delta(a,b,c)))/(2*a)
		x2 = (-b + mt.sqrt(delta(a,b,c)))/(2*a)
		if(x1>x2):
			return x1
		else:
			return x2
	else:
		return -1
"""
we calculate the lower root if delta>0
"""
def xL(a,b,c):
	if(delta(a,b,c) > 0):
		x1 = (-b - mt.sqrt(delta(a,b,c)))/(2*a)
		x2 = (-b + mt.sqrt(delta(a,b,c)))/(2*a)
		if(x1>x2):
			return x2
		else:
			return x1
	else:
		return -1
"""
we calculate the unique root if delta==0
"""
def x0(a,b,c):
	if(delta(a,b,c) == 0):
		return -b/(2*a)
	else:
		return -1

"""
we solve the equation
"""
def solver(a,b,c):
	if(delta(a,b,c)>0):
		print("there are two solutions\n")
		print(xG(a,b,c))
		print(xL(a,b,c))
	elif (delta(a,b,c) == 0):
		print("there is only one solution\n")
		print(x0(a,b,c))	
	else:
		print("there is no solution")
	
"""
we write the polynome in a mathematial form
"""
def polynome(a,b,c):
	if(a == 1):
		stringA = "x²"
	elif(a == -1):
		stringA = "-x²"
	else:
		stringA = "{}x²"

	if (b == 1):
		stringB = "x"
	elif(b == -1):
		stringB = "-x"
	elif(b<0 and b!=-1):
		stringB = "-{}x"
		b = abs(b)
	elif(b == 1):
		stringB = "x"
	else:
		stringB = "+{}x"
		
	string = stringA + stringB + "{}"
	return string.format(a,b,c)


"""
we factorize the polynom
"""
def facto(a,b,c,x0,xG,xL):
	if(delta(a,b,c)>0):
		if (xG > 0):
			stringXG = "{}(x - {})"	
		else:
			xG= abs(xG)
			stringXG = "(x + {})"
		if (xL > 0):
			stringXL = "(x - {})"
		else:
			xL = abs(xL)
			stringXL = "(x + {})"
			
		string = stringXG + stringXL
		return string.format(a,xG,xL)
	elif(delta(a,b,c)==0):
		if (x0 > 0):
			stringX0 = "{}(x-{})"
		else:
			x0 = abs(x0)
			stringX0 = "{}(x + {})²"
		string = stringX0
		return string.format(a,x0)
	else:
		return "no factorization possible"
		

"""
we give a mathematical expression of the factorization
"""
def presentation(a,b,c,x0,xG,xL):
		string1 = polynome(a,b,c) 
		string2 = facto(a,b,c,x0,xG,xL)
		return string1+ " = " +string2  
	

a = int(input("Enter a first value\n"))	
b = int(input("Enter a second value\n"))
c = int(input("Enter a third value\n"))
solver(a,b,c)
print(polynome(a,b,c))
print(facto(a,b,c,x0(a,b,c),xG(a,b,c),xL(a,b,c)))
print(presentation(a,b,c,x0(a,b,c),xG(a,b,c),xL(a,b,c)))

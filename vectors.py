
class vectorClass:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y 
		self.z = z


	def __mul__(self, other):  
		
		if isinstance(other, vectorClass):
			return vectorClass(self.x * other.x,
								self.y * other.y,
								self.z * other.z)


		elif isinstance(other, (int, float)):
			return vectorClass(self.x * other, 
								self.y * other,
								self.z * other)


	def __add__(self, other):  
		
		if isinstance(other, vectorClass):
			return vectorClass(self.x + other.x,
								self.y + other.y,
								self.z + other.z)


		elif isinstance(other, (int, float)):
			return vectorClass(self.x + other, 
								self.y + other,
								self.z + other)		

	def __sub__(self, other):  
		
		if isinstance(other, vectorClass):
			return vectorClass(self.x - other.x,
								self.y - other.y,
								self.z - other.z)


		elif isinstance(other, (int, float)):
			return vectorClass(self.x - other, 
								self.y - other,
								self.z - other)		

	def __truediv__(self, other):  
		
		if isinstance(other, vectorClass):
			return vectorClass(self.x // other.x,
								self.y // other.y,
								self.z // other.z)


		elif isinstance(other, (int, float)):
			return vectorClass(self.x // other, 
								self.y // other,
								self.z // other)		

	def __str__(self):
		return f"V3 = {self.x}:{self.y}:{self.z}"



operation = input("რა ოპერაციის განხორციელება გსურთ? (+, -, *, /) ")


v1X = int(input("შეიტანეთ პირველი ვექტორის X კოორდინატი: "))
v1Y = int(input("შეიტანეთ პირველი ვექტორის Y კოორდინატი: "))
v1Z = int(input("შეიტანეთ პირველი ვექტორის Z კოორდინატი: "))

v1 = vectorClass(v1X, v1Y, v1Z)


option = input("ვექტორს შეიტანთ თუ რიცხვს? (V ან N) ")

if option == "V":

	v2X = int(input("შეიტანეთ მეორე ვექტორის X კოორდინატი: "))
	v2Y = int(input("შეიტანეთ მეორე ვექტორის Y კოორდინატი: "))
	v2Z = int(input("შეიტანეთ მეორე ვექტორის Z კოორდინატი: "))

	v2 = vectorClass(v2X, v2Y, v2Z)

elif option == "N":

	number2 = int(input("შეიტანეთ რიცხვი: "))
	v2 = number2



if operation == "+":
	v3 = v1 + v2
elif operation == "-":
	v3 = v1 - v2
elif operation == "*":
	v3 = v1 * v2
elif operation == "/":
	v3 = v1 / v2


print(v3)
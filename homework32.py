# class Person:
# 	def __init__(self,name,age,sex):
# 		self.name = name
# 		self.age = age
# 		self.sex = sex
# 	def myfunc(self):
# 		print('hello my name is ',self.name,'i am ',self.age,'yers old','my sex is ',self.sex)
# res = Person('Levon',27,"female")
# res.myfunc()
# # print(res.name)
# # print(res.age)
# # print(res.sex)			




# class Car:
# 	def __init__(self,model,year):
# 		self.model = model
# 		self.year = year
# 	def myfunc(self):
# 		print('my car is ',self.model,'produced by ',self.year)

# res = Car('Lexus',2007)
# res.myfunc()	




# class Change:
# 	def __init__(self,euro,rub,amd):
# 		self.euro = euro
# 		self.rub = rub
# 		self.amd = amd
# 	def myfunc(self):
# 		print('Change Usd Euro,Usd Rub,Usd Amd')

# res = Change('euro','rub','amd')
# usd = float(input('Usd: '))
# euro = usd * 1.22
# print(euro,'Euro')
# rub = usd * 73
# print(rub,'Rub')
# amd = usd *512
# print(amd,'Amd')
# res.myfunc()


# class Calculator:
# 	""" It is a calculator class """

# 	def __init__(self, x,choice,y):
# 		self.x = x
# 		self.choice = choice
# 		self.y = y

# 	def add(self):
# 		return self.x + self.y	

# 	def minus(self):
# 		return self.x - self.y	

# 	def mult(self):
# 		return self.x * self.y

# 	def div(self):
# 		return	self.x / self.y


# error_num = 'Please input number'
# while True:
# 	try:
# 		while True:
# 			try:			
# 				x = float(input('X: '))
# 				break
# 			except ValueError:
# 				print(error_num)	

# 		while True:			
# 			choice = input('+ - / * ')
# 			if choice in '+-/*':
# 				break
# 			else:
# 				print('please input + - / * ')

# 		while True:
# 			try:			
# 				y = float(input('Y: '))
# 				break
# 			except ValueError:
# 				print(error_num)	


# 		res = Calculator(x,choice,y)

# 		if choice == '+':
# 			print(res.add())
# 			break
# 		elif choice == '-':
# 			print(res.minus())
# 			break
# 		elif choice == '*':
# 			print(res.mult())
# 			break
# 		elif choice == '/':
# 			try:
# 				print(res.div())
# 				break
# 			except ZeroDivisionError:
# 				print('no zero')
		
	
# 	except KeyboardInterrupt:
# 		print('\nGood bye')	
# 		break

































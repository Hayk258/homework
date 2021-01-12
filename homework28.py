'''1. Create a python function
factorial and import this
file in another file and
print factorial.'''

# def factorial(n):
# 	num = 1
# 	for i in range(2,n + 1):
# 		num *= i
# 	print(num)



'''Write a Python function to
calculate surface volume and area of
a cylinder(Գլան).
V=πr^2h and A=2πrh+2πr^2 '''



# def glan(cylinder,glan1):
# 	pi=22/7
# 	height = float(input('Height of cylinder: '))
# 	radian = float(input('Radius of cylinder: '))
# 	volum = pi * radian * radian * height
# 	sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)

# 	print('Volume is:',volum)
# 	print("Surface Area is: ",sur_area)
# glan(1,5)



'''Write a Python function
to calculate surface volume
and area of a sphere.
V = 4/3*π*r3 and A = 4*π*r2'''


# def volumee(radian):
# 	pi=22/7
# 	sur_area = 4 * pi * radian **2
# 	volume = (4/3) * (pi * radian ** 3)

# 	print("Surface Area is: ", sur_area)
# 	print("Volume is: ", volume)


'''Write a Python function to print
all primes smaller than or equal to a
specified number.
Call function:numbers(9)
Output: (2, 3, 5, 7)
'''


def function(n):
	for i in range(2,10):
		for j in range(2,i):
			if i %j == 0:
				break
		else:
			print(i)






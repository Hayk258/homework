'''1. km to mile
Write a python function which
conversion kilometer to miles.'''


# def km_to_ml(km):
# 	res = km/1.6
# 	return res
# km = int(input('km: '))
# print(km_to_ml(km))


'''2. Time
Write a python function which
conversion days to seconds.'''


# def deys_second(deys):
# 	res = deys * 24 * 60 * 60
# 	return res
# deys = int(input('days: '))
# print(deys_second(deys),'seconds')



'''3. Password
Write a python function which
generate a valid password.'''



# def valid_password(password):
# 	count = 0
# 	char = 0
# 	if len(password) >= 8:
# 		for i in password:
# 			if i.isdigit():
# 				count += 1
# 			elif i.isalpha():
# 				char += 1
# 		if count > 1 and char > 1:
# 			return 'your password is strong '
# 		else:
# 			return 'your password is not strong '
# 	else:
# 		return 'your password length then 8 '
# password = input('please enter password ')
# print(valid_password(password))



'''Factorial'''

# import math
# def fac(n):
# 	res = math.factorial(n)
# 	return res

# n = int(input('factorial: '))
# print(fac(n))


'''Given an list of numbers.
Find the maximum element in
list.Without use max function'''



# def max_num(num):
# 	num.sort()
# 	return num[-1]


# num = [1,66,7,8,33,99,87,1,2,3,4,5]
# print(max_num(num))




'''Blot'''

import random

def calod():
	""" stexcumenq kalod xaxaqarterov """

	mast = ('♣ ', '♦ ', '♥ ', '♠ ')
	cards = ('9','10','J','Q','K','T')
	res = []
	for i in mast:
		for j in cards:
			x=i+j
			res.append(x)
	random.shuffle(res)
	return res	

# print(calod())


def user():
	""" talis enq userin xaxaqarter """

	global res
	user_cards = []
	res = calod()
	for i in range(5):
		x = res.pop()	
		user_cards.append(x)
	user_cards.sort()		
	return user_cards	


print('User-- ',user())


def pc():
	""" talis enq pc in xaxaqarter """

	pc_cards = []
	for i in range(5):
		x = res.pop()	
		pc_cards.append(x)
	pc_cards.sort()		
	return pc_cards	


print('\nPc-- ',pc())


def tramp_card():

	x = res.pop()
	return x





def new_card():
	q = tramp_card()

	print('\ntramp card-- ',q)
	useri = input('Want you take tramp card ') == 'y'
	if useri:
		c = user()
		y = pc()
		c.append(q)
		for i in range(2):
			x = res.pop()
			c.append(x)
		print('user',c)
		for i in range(3):
			x = res.pop()
			y.append(x)
		print('pc',y)	
	else:
		pci = input('Want pc take tramp card ') == 'y'
		if pci:
			c = user()
			y = pc()
			y.append(q)
			for i in range(2):
				x = res.pop()
				y.append(x)
			print('pc',y)
			for i in range(3):
				x = res.pop()
				c.append(x)
			print('user',c)


new_card()
# print(user())






































































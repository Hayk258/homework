# def new_list(a,b,step):
# 	c =[]
# 	for i in range(a,b,step):
# 		c.append(i)
# 	return c

# a = int(input('a: '))
# b = int(input('b: '))
# step = int(input('step: '))


# print(new_list(a,b,step))




# def my_list(n):
# 	c = []
# 	for i in range(len(n)-1):
# 		res = n[i]*n[i+1]
# 		c.append(res)
# 	return c
# list2 = [1,3,5,6,7]

# print(my_list(list2))


# def word(my_word,my_list):
# 	count = 0
# 	my_word = list(my_word)
# 	for i in range(len(my_word)):
# 		if my_word[i] == '_':
# 			my_word[i] = my_list[count]
# 			count += 1
# 	return ''.join(my_word)

# my_word = '_ we have a _'
# my_list = ['Houston','Problem']

# print(word(my_word,my_list))



# def sum(list_of_string):
# 	res = [len(i) for i in list_of_string]
# 	result = min(res)+max(res)
# 	return result


# list_of_string = ['anymore', 'raven', 'me', 'communicate'] 

# print(sum(list_of_string))


# def res(my_list,number):
# 	count = 0
# 	c = []
# 	if number in my_list:
# 		print(my_list.index(number))
# 	else:
# 		for i in my_list:
# 			res = abs(i-number)
# 			c.append(res)
# 		x =min(c)
# 		print(c.index(x))
			



# my_list = [21, -9, 15, 2116, -71, 33]
# number = -8
# res(my_list,number)




'''Define a function which can generate a dictionary where
the keys are numbers between 1 and N (both included) and
the values are square of keys. The function should print the
dict.Example'''



# def my_func(x):
# 	c = dict()
# 	for i in range(1,20):
# 		c[i]=i**2
# 	return c	

# new_list = {}

# print(my_func(new_list))




# def num(number,n):
# 	odd = 0
# 	even = 0
# 	for i in range(n,number):
# 		if i %2 == 1:
# 			odd +=1 		
# 		else:
# 			even += 1
# 	return odd,even			
# number = int(input('number: '))
# print(num(number,n = 0))



def num(x,y):
	res = x*y
	for i in range(1,res + 1):
		if i %x == 0 and i %y == 0:
			print(i)
			break
x = 12
y = 15

num(x,y)

	







































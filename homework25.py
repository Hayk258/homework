# file_name = 'Ararat.txt'
# f = open(file_name,'a')
# login = input('Login: ')
# mail = input('mail: ')
# password = input('password: ')
# res = '\nlogin ' + login +'\nmail ' + mail +'\npassword ' + password
# f.write(res)


# file_name2 = 'Hayastan.txt'
# f = open(file_name2,'w')
# age = input('age: ')
# name = input('name: ')
# year = input('year: ')
# res = '\nage '+ age +'\nname '+name+'\nyear '+year
# f.write(res)



# file_name3 = 'ekb.txt'
# f = open(file_name3,'w')
# city = input('your city: ')
# car = input('car: ')
# languege = input('languege: ')
# res = '\ncity '+city + '\ncar '+car+'\nlanguege '+languege
# f.write(res)


# file_name4 = 'iphone.txt'
# f = open(file_name4,'w')
# phone = input('phone: ')
# notebook = input('notebook ')
# color = input('color ')
# res = '\nphone ' + phone + '\nnotebook ' + notebook + '\ncolor ' + color
# f.write(res)


# file_name5 = 'password.txt'
# f = open(file_name5,'w')
# number = input('number: ')
# year = input('year: ')
# country = input('country: ')
# res = '\nnumber '+number+'\nyear '+year+'\ncountry '+country
# f.write(res)




'''Write a Python program to read first n lines of
a file.'''


# file_name6 = 'Python.txt'
# f = open(file_name6, 'w')
# res= 'Hayk live in moscow'
# f.write(res)
# f.close()
# f = open(file_name6)
# c = f.readline().split()
# print(c)




'''Write a Python program to append text to a file and
display the text'''




# file_name7 = 'Tokyo.txt'
# f = open(file_name7,'w')
# city = input('enter your city: ')
# f.write(city)
# f.close()
# f = open(file_name7)
# print(f.read())
# f.close()

# with open("test.txt", "a") as myfile:
#     myfile.write("appended text")



'''Write a python program to find the longest words'''

# f = open('Ararat.txt')
# c = []
# for i in f:
# 	c.append(len(i))
# print(c)
# f = open('Ararat.txt')
# for i in f:
# 	if len(i) == max(c):
# 		print(i)new_file = 'ekb.txt'




'''Write a python program to find numbers in txt.
'''


# f = open(new_file,'w')
# year = input('year: ')
# f.write(year)
# f.close()
# f = open(new_file)
# num = 0
# for i in f:
# 	for c in i:
# 		if c.isdigit():
# 			num += 1
# print(num)






new_file = 'ekb.txt'
f = open(new_file,'w')
year = input('year: ')
f.write(year)
f.close()
f = open(new_file)
num = 0
for i in f:
	for c in i:
		if c.isdigit():
			num += 1
print(num)



'''Write a python program to get login and password.'''


# file_name8 = 'password.txt'
# f = open(file_name8,'w')
# login = input('login: ')
# password = input('password: ')
# res = '\nlogin '+login+'\npassword '+password
# f.write(res)























































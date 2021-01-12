import json
'''1. Dict
You have two list convert it in dictionary and add
in (mydict.txt) and show result:'''


# anun = ['Ani','Anna','Elen']
# tiv = [1,2,3]

# x = zip(tiv,anun)
# c = dict(x)


# def add_in_file(file_name,c):
# 	with open(file_name,'w') as f:
# 		json.dump(c,f)
# add_in_file('new.json',c)


'''Create json file and save them lyrics (song)
and print in cmd word this song.'''


# def song(file,barer):
# 	with open(file,'w') as f:
# 		json.dump(barer,f)
# 	f = open(file)
# 	print(json.load(f))

# file = 'Song.json'
# barer = 'Tell me somethimg boy are you happy in this modern world \nor do you need more'

# song(file,barer)



'''Write a python program which have one input an
integer, representing the sum of all the multiples of
3 and 5 below the given input. and save this result
in json file.
for example: '''


# def sumnum():
# 	num = int(input('num: '))
# 	res = []
# 	for i in range(1,num):
# 		if i %3 == 0 or i % 5 == 0:
# 			res.append(i)
# 	with open('a.json','w') as f:
# 		json.dump(sum(res),f)
# sumnum()				



''' Write a program that takes in a string as input,
counts and outputs the number of vowels.
And add result in json file.'''


# def vavel(file,bar):
# 	dzaynavorner = 'aeiouy'
# 	count = 0
# 	for i in bar:
# 		if i in dzaynavorner:
# 			count += 1
# 	with open(file,'w') as f:
# 		json.dump(count,f)

# bar = input('bar: ')
# vavel('i.json',bar)		




'''You have text.txt file and contains such text:
Another pause and more eying and siding around
each other
You can create one dict where you have.
‘’another’’:1
‘’and’’:2
'''



# def res(file):
# 	with open(file,'w')as f:
# 		text = 'Another pause and more eying and siding around each other'
# 		f.write(text)


# 	result = {}
# 	with open(file)as f:
# 		for i in f.read().split():
# 			if i in result:
# 				result[i] = result[i] + 1
# 			else:
# 				result[i] = 1
# 	return result
# print(res('text.txt'))			




'''Write a python function which get a new list
from a given list, consisting of the first
repeating elements.
my_list = [“a”,”b”,”a”,”c”,”b”]
output “a”,”b”,”c”
'''



# def new_list(file,old_list):
# 	new = []
# 	for i in old_list:
# 		if i not in new:
# 			new.append(i)
# 	with open(file,'w') as f:
# 		f.write(i)

# new_list('aaa.txt',['a','b','a','c','b'])


'''You have word.txt file and in them you have
one story.
Write a Python function that accepts this
story and calculate the number of uppercase
letters and lowercase letters. '''



# def one_story(story):
# 	mecatar = 0
# 	poqratar = 0
# 	for i in story:
# 		if i.isupper():
# 			mecatar += 1
# 		elif i.islower():
# 			poqratar += 1
# 	print(mecatar,poqratar)		


# story = input()
# one_story(story)















































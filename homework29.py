# def factorial(x):
# 	if x == 0:
# 		return 1
# 	elif x == 1:
# 		return 1
# 	else:
# 		return x * factorial(x-1)
# print(factorial(4))			



# def fibonachi(x):
# 	if x == 1:
# 		return 0
# 	elif x == 2:
# 		return 1
# 	else:
# 		return fibonachi(x-1)+fibonachi(x-2)
# print(fibonachi(5))	



# def liner_cearch(my_list,n,x):
# 	for i in range(0,n):
# 		if my_list[i] == x:
# 			return i
# 	return -1
# my_list = [1,2,3,66,77,88,9,33,45,78,11]
# x = 78
# n = len(my_list)
# result = liner_cearch(my_list,n,x)

# if result == -1:
# 	print('dzer tivy chi hamapatasxanum:')
# else:
# 	print('dzer tivn e ',result)	



# def binery_search(my_list,search,start,stop):
# 	if start > stop:
# 		return False
# 	else:
# 		mid = (start + stop)//2
# 		if search == my_list[mid]:
# 			return mid
# 		elif search < my_list[mid]:
# 			return binery_search(my_list,search,start,mid+1)
# 		else:
# 			return binery_search(my_list,search,mid-1,stop)

# start = 0
# search = 156
# my_list = [1,3,7,8,23,45,67,156,300,567,990,1020]
# stop = len(my_list)

# result = binery_search(my_list,search,start,stop)

# if search == False:
# 	print('iteam',search,'not found')
# else:
# 	print('iteam',search,'found at indexs',result)


old_list = [10,75,43,15,25,-4,27]

def bublle_sort(my_list):
	last_iteam = len(my_list)-1
	for i in range(0,last_iteam):
		for j in range(0,last_iteam-i):
			if my_list[j] > my_list[j+1]:
				my_list[j],my_list[j+1]= my_list[j+1],my_list[j]

	return my_list

print('old_list',old_list)
new_list = bublle_sort(old_list).copy()
print('new_list',new_list)			

































# import threading
# import time 


# def gender(file_name,start,end):
# 	with open(file_name)as f:
# 		for line in f.readlines()[start:end]:
# 			info = line[:-1].split(',')
# 			if info[3] == 'male':
# 				with open('males.txt','a')as malef:
# 					malef.write(line)
# 			elif info[3] == 'female':
# 				with open('female.txt','a')as femalef:
# 					femalef.write(line)
# 			time.sleep(0.1)	

# file_name = 'users.txt'
# start = time.time()

# t1 = threading.Thread(target = gender,args = (file_name,1,33))
# t2 = threading.Thread(target = gender,args = (file_name,34,66))
# t3 = threading.Thread(target = gender,args = (file_name,67,100))
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# end = time.time()
# print(end-start)
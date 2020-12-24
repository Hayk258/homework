def valid_password(password):
	count = 0
	num = 0
	if len(password) < 8:
		raise ValueError('your password lenght then 8')
	else:

		for i in password:
			if i.isdigit():
				count += 1
			elif i.isalpha():
				num += 1
		if count > 1 and num > 1:
			return 'your password is strong'
		else:
			return 'your password is not strong'

password = input('please enter password:  ')
print(valid_password(password))


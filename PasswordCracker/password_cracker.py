import string
# user_password = str(raw_input("Enter a password: "))
checker = True
# while checker:
# 	guess = ''
# 	for index in range(len(user_password)):
# 		for char in string.printable:
# 			if guess is user_password:
# 				print "Your password is %s " % guess
# 				checker = False	
# 		
# 			elif char == user_password[index]:
# 				print char
# 				print guess
# 				guess+=(char)
# 				
alpha = []
word = 'wor'
splitted = list(word)
#print splitted
guess = ''
while guess != word:
	for char in string.printable:
		if guess is word:
			print guess, word
			
		if char in splitted:
			guess+=(char)
			break
		

	# 	
# 	else:
# 		for index in range(len(user_password)):
# 			for char in string.printable:
# 				if char == user_password[index]:
# 					print char
# 					guess+=(char)
# 					print guess
# 					checker = False
# 				else:
# 					break
# 					print guess
# 			




# 
# 
# 
# import string
# password = raw_input("Enter a password: ")
# 
# def passCrack(password, guess):
# 	if(len(guess) == len(password)):
# 		if guess == password:
# 			print "Your password is %s " % password
# 	else:
# 		for letter in string.printable:
# 			passCrack(password, guess+letter)
# 
# for letter in string.printable:
# 	passCrack(password, letter)
from random import *
#num = randrange(0,100)
#print num

#number guesser
number = int(input("enter a number between 1 and 100 >>> "))
def divider(number):
	runner = True
	low = 0
	upp = 100
	guess = randrange(low,upp)
	print guess
	while (guess != number and runner==True):
		
		if guess == number:
			print "your number is %r" % number
			runner = False
		
		else:
			answer = raw_input("is your number > %r: " % guess) 
			if answer == "yes" or answer == "Yes":
				low = guess
				guess = randrange(guess,upp)
				print low, upp, guess
				#return guess

			elif answer == "no" or answer == "No":
				upp = guess
				guess = randrange(low,guess)
				print low, upp, guess
				#return guess
				#print 'Your number is %r' % number

		#print 'Your number is %r' % number

			
divider(number)
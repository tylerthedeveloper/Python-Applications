#Programmer: Tyler Citrin
import string

password = raw_input("Please enter your password: ")

def breathFirstPassword(password, guess):
    if(len(guess) == len(password)):
        if(guess == password):
            print "password found as " + password
            exit
    else:
        for letter in string.printable:
            breathFirstPassword(password, guess+letter)

def depthFirstPassword(password):
    depth = 1
    while(guess != password):   
        for letter in string.printable:
                a-z
                for letter in string.printable:
                    a-z

        print "password found as " + password
        exit
    else:
        for letter in string.printable:
            depthFirstPassword(password, guess+letter)

def generateStrings(base, depth):
    
    return # list of possible strings
                

depthFirstPassword(password)

#print password

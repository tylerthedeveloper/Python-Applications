from itertools import *
import re
from Tkinter import *
import tkMessageBox

#div_calculator 2.0
# "X(5x^2)^2"

power = 0
power1 = 0
var = ''
var1 = ''
#(5x^2)
inExp = ''




#def derive()
# create 3 variables of each expression

def stepOne():
	if '(' in expression:
		inExp = expression[expression.find("(")+1:expression.find(")")]
		stepOne.num1 = inExp.rsplit('x',1) # only want [0] as below, not array...
		#return stepOne.num1
			# ^need to make for all variables, not just x
		if '^' in inExp:
			power1 = inExp.rsplit('^',1) # only want [0] as below, not array...
			stepOne.powerPrint1 = int(power1[1])
			#return stepOne.powerPrint1
		else:
			stepOne.powerPrint1 = 0
	
		var1 = re.search(r'[a-zA-Z]', inExp)
		try:
			stepOne.varPrint1 = var1.group()
			return stepOne.varPrint1
		except:
			varPrint1 = '' # none
			return stepOne.varPrint1
	else:
		return None


def calc():
	# (5y^2)(3x^2)
	# x^2 * sin(x)
	#  f     g
	# f*g' + g*f'
	num = expression.rsplit('x',1) # only want [0] as below, not array...
 	# ^need to make for all variables, not just x
	#print num[0]
	
	if '^' in expression:
		power = expression.rsplit('^',1) # only want [0] as below, not array...
		powerPrint = int(power[1])
 	else:
	 	powerPrint = 0
		
	var = re.search(r'[a-zA-Z]', expression)
	try:
		varPrint = var.group()
	except:
		varPrint = '' # none

	if stepOne() != None:
		# combine inExp with Expression
		print 'hi'
		print stepOne.num1, stepOne.powerPrint1, stepOne.varPrint1 
		# 	
		if stepOne.powerPrint1 == 1:
			print int(num1[0])*int(num[0]), varPrint1, 
# 			
# 		elif stepOne.powerPrint1 == 0:
# 			powerPrint1 = int(num1[0])
# 			print int(num1[0])

# 		else:
# 			print = (int(num1[0])*int(powerPrint1)) , varPrint1 ,  '^' , (powerPrint1-1) 			

		
	else:	
		if powerPrint == 1:
			print int(num[0]), varPrint
			
		elif powerPrint == 0:
			print int(num[0])
			
		else:
			print (int(num[0])*int(powerPrint)) , varPrint ,  '^' , (powerPrint-1)	
		








def stepTwo():
#5 + (5x+10y)
#5 , 5x 10y
# split expression into separate objects
# stuff in and outside of expression
#	listTest =[]
 	for index in range(len(expression)):
#		while exp <= len(expression)-1:
# 			if '(' in expression:
# 				exp = expression[expression.find("(")+1:expression.find(")")]
# 				if '+' or '-' in exp:
#		listTest.append(index)

# 		if "cos" in expression:
# 			exp = expression[expression.find("cos(")+4:expression.find(")")]
# 			expList.append(exp)
# 		if 'sin' in expression:
# 			exp = expression[expression.find("sin(")+1:expression.find(")")]

# 		if 'tan' in expression:
# 			exp = expression[expression.find("tan(")+1:expression.find(")")]

		
		exp = re.split("[+-]", expression)
#		print exp
		expList.append(exp)
# 		expTest = re.split(" ", expression)
# 		expTest.append(expTest)
		#print expList[index]
				# else:
					#expList.append(exp)
# 			else:
# 				exp = re.split("([+-])", expression)
# 				expList.append(exp)						
		return expList[0][:] #, listTest



#expression = raw_input("Please enter your expression: ")
# signList = []			


#expression = ''

Deriver = Tk()	
def GUI():

	L1 = Label(Deriver, text="Please enter an expression to be derived:").grid(row=0, sticky=W, column=0)
	var = StringVar()
	global E1
 	E1 = Entry(Deriver, textvariable=var)
	E1.grid(row=0, column=1)
	B1 = Button(Deriver, text = "DERIVE", command = derive).grid(row=0, column=2)
	B2 = Button(Deriver, text = "DONE", command = terminate).grid(row=0,column=3)
	global textList
	textList = Text(Deriver, height=5)
	textList.grid(row=1, column=0, columnspan=4)	

def terminate():
	sys.exit()


#Deriver = Tk()	

def derive():

	t = True
	
	
	# L1 = Label(Deriver, text="Please enter an expression to be derived:").grid(row=0, sticky=W, column=0)
# 	var = StringVar()
# 	global E1
# 	E1 = Entry(Deriver, textvariable=var)
# 	E1.grid(row=0, column=1)
# 	B1 = Button(Deriver, text = "DERIVE", command = derive).grid(row=0, column=2)
# 	B2 = Button(Deriver, text = "DONE", command = terminate).grid(row=0,column=3)
# 	global textList
# 	textList = Text(Deriver, height=5)
# 	textList.grid(row=1, column=0, columnspan=4)
	
	while t:
	
		expList = []

		expression = E1.get()

		derivative = []
	
		signList = re.findall(r"[(+\-)]", expression)
	#	print signList
	
		for exp in range(len(expression)):
# 			if "cos" in expression:
# 				exp = expression[expression.find("cos(")+4:expression.find(")")]
	# 			expList.append(exp)		
			exp = re.split("[+-]", expression)
			expList.append(exp)

	#		while exp <= len(expression)-1:
	# 			if '(' in expression:
	# 				exp = expression[expression.find("(")+1:expression.find(")")]
	# 				if '+' or '-' in exp:

		for exp in expList[0][:]:
			exp = str(exp)
	#		print 'exp is' , exp
			num = exp.split('x') # only want [0] as below, not array...
			# ^need to make for all variables, not just x
			numtest = int(str(num[0][:]))
	#		print 'numtest is ' , numtest

			if '^' in exp:
				power = exp.rsplit('^',1) # only want [0] as below, not array...
				powtest = int(str(power[1][:]))
	#			print 'powtest is ', powtest
			else:
				powtest = 0
			
			var = re.search(r'[a-zA-Z]', exp)
			try:
				varPrint = str(var.group())
			except:
				varPrint = '' # none
		
			if powtest == 1:
				derivative.append(str(numtest) + varPrint)
			elif powtest == 0:
				if varPrint == '':
					derivative.append('')
				else:
					derivative.append(str(numtest))
			else:
				if powtest == 2:
					derivative.append(str((powtest * numtest)) + str(varPrint))
				else:
					derivative.append(str((powtest * numtest)) + str(varPrint) + '^' + str(powtest-1))
	# 			derivative += numtest
	# 			derivative += varPrint
		
		testList = []
	#	print signList
	#	print derivative
		if len(expList[0]) > 1:
			# zip -> not equal on last character ... will not print...
			testList = [item for pair in izip_longest(derivative, signList, fillvalue='') for item in pair]
	#		testList = [filter(None, pair) for pair in izip_longest(derivative,signList)]
			#range(len(signList)), range(len(derivative)):
			#testList += str(signList[i]), str(derivative[i])
	#http://stackoverflow.com/questions/11318977/zipping-unequal-lists-in-python-in-to-a-list-which-does-not-drop-any-element-fro
			x = ''.join(testList)		
			if x[-1] == '+' or x[-1] == '-':
				tkMessageBox.showinfo("Derivative", x[:-1])
				textList.insert(END, ("Derivative of " + expression + ' is ' + x[:-1] + '\n'))
				E1.delete(0, END)
 				t = False
 				return False
			else:	
				tkMessageBox.showinfo("Derivative", x)
				textList.insert(END, ("Derivative of " + expression + ' is ' + x + '\n'))
				E1.delete(0, END)
				t = False
				return t
				#return False
			# for index in expList:
			#	expList[index] = derivative

		else:
			y = str(''.join(derivative))
			tkMessageBox.showinfo("Derivative", y)
			textList.insert(END, ("Derivative of " + expression + ' is ' + y + '\n'))
			E1.delete(0, END)
# 			derivative = []
# 			expression = ''
#			derive()
			t = False
			return t
		
		#	expression.replace(expression.find('+'), 'x')	
		#	print derivative









#stepTwo()
#derive()

#		print expression
# 		if '+' or '-' in expression:
# 			print 'hi'
# take expList ... leave plus or minus signs 
# take exp, derive, return to list .replace ... 
# explist[exp].replace(derive(exp))
			
		
#(int(num[0])*int(powerPrint)) , varPrint ,  '^' , (powerPrint-1)	
#	print expList[0][1]
#	print derivative #, ' hi'
#	derivative+=exp

#derivative = 
# 		print num[0]
# 		print powerPrint
# 		print varPrint
		
		
#stepOne()
#calc()

def main():
#	derive()
	GUI()
	Deriver.mainloop()
	
if __name__ == "__main__":
    main()


# errors:
			
# 1. trig functions ...
# 2. looping until done...
# 3. 5x+3x ... should be 8x
# 	5x + 3x = 5 + 3 = 8
# stuff in parantheses)
# 4. one textbox with question and answers below it
# if parantheses and nothing in front AND back, drop
# ^ if only front
# ^ if only back
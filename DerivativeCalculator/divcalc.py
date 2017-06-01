#div_calculator
# first = int(raw_input("Please enter the leading int of the expression: "))
# var = str(raw_input("Please enter variable int of the expression: "))
# power = int(raw_input("Please enter the exponent of the expression: "))

# "5x^2"
# "5 , (3x^2), ^ 2
# ['5','x','^','2',0]
expression = raw_input("Please enter your expression: ")

package = expression.split('^')
print package

num = package[0][0:len(package[0])-1]
print num

var = package[0][len(package[0])-1]
print var

exp = int(package[1])
print exp

def calc(num, var, exp):
 	
 	if len(str(num)) == 0:
 		num = 1
	
	back_exp=exp-1
	if back_exp == 1:
  		print (exp*int(num)),var
  	else:
  		print (exp*int(num)),var,'^',(back_exp)
	
calc(num, var, exp)
def factorial(num):
#Check for negative integers
	if num < 0:
		return "Factorial can't be negative."

#Base Case
	if num == 1:
		return num
#Recursive Case
	else:
		num * factorial(num - 1)
	

def palindrome(string):
	pass

def bottles(num):
	pass

def roman_num(num):
	pass

print(factorial('g'))
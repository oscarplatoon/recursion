
#In theory each function would be its own file

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
	#Variable to hold reverse of string
	test = string[::-1]

	#Base Case
	if test == string:
		return 'This is a palindrome'
	#Recursive Case
	else:
		return 'This is not a palindrome'
	

def bottles(num):
	#Base Case
	if num == 1:
		return 'No more bottles'

	#Recursive Case to account for bottles to bottle
	elif num == 2:
		print(f'{num} bottles of beer on the wall, {num} bottles of beer.')
		print(f'Take one down and pass it around, {num - 1} bottle of beer on the wall.')
		return bottles(num - 1)

	#Recursive Case
	else:
		print(f'{num} bottles of beer on the wall, {num} bottles of beer.')
		print(f'Take one down and pass it around, {num - 1} bottles of beer on the wall.')
		return bottles(num - 1)
		

def roman_num(num):
	pass


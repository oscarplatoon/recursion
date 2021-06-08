import re

def palindrome(string):
	
	word = re.sub("\W", '',str(string).lower())
	print(word)
	if len(word)<=1:
		return True
	if word[0]==word[-1]:
		return palindrome(word[1:-1])

print(palindrome('ra ce Car'))



# def factorial(x):
# 	pass

# def bottles(num):
# 	pass

# def roman_num(num):
# 	pass
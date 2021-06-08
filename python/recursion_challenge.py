import re


def factorial(x):
	pass


# allow your palindrome checker to check against palindromes sentence such as,
#
# "Sore was I ere I saw Eros."
# "A man, a plan, a canal -- Panama"

# get rid of spaces, special characters, etc.
# BASE CASE
# if length of word is 1 character return true
# RECURSIVE CASE
# if first char == last char
	# return palindrome(word[1:-1])

# racecar
# aceca
# cec

# 1. Base case
# 2. Recursive case
def palindrome(string):
	word = re.sub('\W', '', str(string).lower())
	if len(word) <= 1:
		return True
	if word[0] == word[-1]:
		return palindrome(word[1:-1])
	return False

print(palindrome(""))


def bottles(num, original):
	new_num = num
	# recursive case
	if num >= 1:
		print(f"{new_num} bottle{'s' if (new_num > 1) else ''} of beer on the wall, {new_num} bottle{'s' if (new_num > 1) else ''} of beer.")
		new_num -= 1
		if new_num > 0:
			print(f"Take one down and pass it around, {new_num} bottle{'s' if new_num > 1 else ''} of beer on the wall.")
			# return bottles(new_num, original)
		return bottles(new_num, original)
	# base case
	else:
		print('Take one down and pass it around, no more bottles of beer on the wall.')
		print('No more bottles of beer on the wall, no more bottles of beer.')
		print(f'Go to the store and buy some more, {original} bottles of beer on the wall.')

bottles(5, 5)

def roman_num(num):
	pass
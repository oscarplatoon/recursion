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
	else:
		return False

print(palindrome("A man, a plan, a canal -- Panama"))
print(palindrome("a"))


def bottles(num):
	pass

def roman_num(num):
	pass
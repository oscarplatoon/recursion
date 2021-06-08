def factorial(x):
	list = 1
	if type(x) == str:
		return "Please input a number"
	if x <= -1:
		return "Please input a non negative integer"
	for number in range(x):
		list = list * (number + 1)
	return list
	

def palindrome(string):
	pass

def bottles(num):
	plural = "bottles"
	single = "bottle"
	if num > 0:
		print(f"{num} {single if num == 1 else plural} of beer on the wall, {num} {single if num == 1 else plural} of beer. You take one down, pass it around. {num - 1} {single if num - 1 == 1 else plural} of beer.")
		bottles(num - 1)
	else:
		return("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

def roman_num(num):
	pass

# bottles(100)
factorial(8)


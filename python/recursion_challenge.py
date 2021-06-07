def factorial(num, total = 1):
    if num <=1:
        return total
    else:
        total = total*num
        print(total)
        return factorial(num-1, total)

print(factorial(5))

def palindrome(string):
	pass

def bottles(num, str):
    #Base case:
    if num == 0:
        str += "No more bottles of beer on the wall, nor more bottles of beer. \n"
        str += f"Go to the store and buy some more, 99 bottles of beer on the wall."
        return str

    if num == 1:
        str += f"{num} bottle of beer on the wall, {num} bottle of beer.\n"
        str += f"take one down and pass it around, no more bottles of beer on the wall. \n"
        num -= 1
        return bottles(num, str)

    if num == 2:
        str+=(f"{num} bottles of beer on the wall, {num} bottles of beer. \n")
        str+=(f"take one down, pass it around, {num-1} bottle of beer on the wall.\n")
        num -= 1
        return bottles(num, str)

    if num > 2:
        str += f"{num} bottles of beer on the wall, {num} bottles of beer.\n"
        str += f"take one down, pass it around, {num-1} bottles of beer on the wall.\n"
        num -= 1
        return bottles(num, str)

def roman_num(num):
	pass

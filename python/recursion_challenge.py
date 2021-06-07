def factorial(num, total = 1):
    # Base case, initialize total to 1, so if no change needed, it returns accurately.
    if num <=1:
        return total
    # Takes default total, and starts multiplying it before recursing with a one
    # less num and the updated total. Return total at each step
    else:
        total = total*num
        return factorial(num-1, total)

def palindrome(string):
    #Clean up input by discarding non alpha characters.
    string = ''.join([i for i in string if i.isalpha()])
    string = string.lower()

    # Base Cases, if the string is down to 0 or 1 characters, the sentence is a palindrome.
    if len(string) <= 1:
        return True

    # Test for equality of first and last character, if equal, slice them off and 
    # rerun palindrome with truncated string. If not equal, return False.
    if string[0] == string[len(string)-1]:
        string = string[1:len(string)-1]
        return palindrome(string)
    else:
        return False

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

# palindrome takes in a string STR, removes all punctuation and spacing, and converts it to lowercase and saves it as CLEAN_STR. Palindrome calls reverse_string on CLEAN_STR to generate a strings reverse. It thens compares the return value of reverse_string to CLEAN_STR
import re

def palindrome_recursive(string):
    if isinstance(string, str):
        clean_str = string.lower()
        clean_str = re.findall('[a-z0-9]', clean_str)
        clean_str = "".join(clean_str)
    else:
        clean_str = str(string)

    reverse_str = reverse_string(clean_str)

    return reverse_str == clean_str

#reverse_string recursively reverses a string by swapping the first and last chars of the string, and calling reverse_string on the remaining string
#base cases are 0 or 1 characters remaining
#if 1 character remains, it returns that character
#if 0 characters remain, it returns '' 
def reverse_string(str):

    if len(str) == 0:
        return ''
    elif len(str) == 1:
        return str
    else:
        return str[-1] + reverse_string(str[1:-1]) + str[0]

    
   


def arabic_to_roman(number, posit = -1):
    roman_numerals = [
        ["I"     , 1],
        ["IV"    , 4],
        ["V"     , 5],
        ["IX"    , 9],
        ["X"     , 10],
        ["XL"    , 40],
        ["L"     , 50],
        ["XC"    , 90],
        ["C"     , 100],
        ["CD"    , 400],
        ["D"     , 500],
        ["CM"    , 900],
        ["M"     , 1000]
    ]
    
    if number == 0:
        return ''
    
    else:
        number_roman_chars = number//roman_numerals[posit][1]
        output = str(roman_numerals[posit][0]*number_roman_chars)
        return output + arabic_to_roman(number - number_roman_chars*roman_numerals[posit][1], posit - 1)

# print(arabic_to_roman(499))
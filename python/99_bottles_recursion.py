# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.
#
# Take one down and pass it around, no more bottles of beer on the wall.
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.

def bottle_song(number_bottles, count = 1):
    if (number_bottles == 1):
        print("Take one down and pass it around, no more bottles of beer on the wall.")
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, {count} bottles of beer on the wall.")
    
    else:
        print(f"{number_bottles} bottle{'s' if number_bottles > 1 else ''} of beer on the wall, {number_bottles} bottle{'s' if number_bottles > 1 else ''} of beer.")
        print(f"Take one down and pass it around, {number_bottles-1} bottle{'s' if number_bottles-1 > 1 else ''} of beer on the wall.")
        bottle_song(number_bottles-1, count+1)

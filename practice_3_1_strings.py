"""
package : practice
chapter : Text data type => str, str(value)
topics  : []
"""
# string is an [array of bytes] like other in python
# Normal
simple_str = "1234567890"

# multi-line string
multiline_str = """
This is           line 1
This     is line 2

This is line 3
This is line 4
"""

# Fomatting + concatenation
detail_str = "This is string concatenation with formatting"

value_1 = 10
value_2 = 10
result = value_1 + value_2

# escape sequence
"""
https://www.w3schools.com/python/python_strings_escape.asp
"""
print('Ikram\'s PC')
print('Ikram\\s PC')
print('Ikram\n PC')
print('Ikram \bPC')

# slicing => [start_index(included):end_index(excluded)] => indexing in str => YES
# VALUES 1   2 3 4 5 6 7 8 9 0
# INDEX  0   1 2 3 4 5 6 7 8 9
# -INDEX -10-9-8-7-6-5-4-3-2-1

print()
print(simple_str[1:10])
print(simple_str[1:11])
print(simple_str[3:140])
print(simple_str[-1])
print(simple_str[-2])
print(simple_str[-10])
print(simple_str[-12])

print()
print(simple_str[0:1])
print(simple_str[0:2])
print(simple_str[2:9])

# length and looping
print(len(simple_str))
for value in simple_str:
    print(value)

# in/not in
print("1" in "1 2 3 4 5")
print("1" not in "1 2 3 4 5")


# String functions
simple_str = "my name is ikram"
print(simple_str.isupper())
print(simple_str.capitalize())
print(simple_str.strip(" "))
print(simple_str.replace('ikram', 'zahida & durani'))

# OUTPUTS
print(simple_str)
print(multiline_str)
print("""
value 1: {}
value 2: {}
result : {}
""".format(value_1, value_2, result))

print("str " + "str1")

"""
Method	           Description
------------------------------
isupper()	    Returns True if all characters in the string are upper case
capitalize()	Converts the first character to upper case
strip()	        Returns a trimmed version of the string
replace()	    Returns a string where a specified value is replaced with a specified value
-----------------------------------------------------------------------------------------------------------
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
"""

"""
package : practice
name    : practice_2_variables.py
chapter : variables
topics  : []
"""

# data_types  -------------------------------------------------------
numeric_type = 100  # ==> int
decimal_type = 1.0  # ==>
complex_type = 1j
text_type = "MARK"  # ==> str
list_type = []  # [list] / {tuple} / range()  # ==> list, tuple, range
tuple_type = ()  # [list] / {tuple} / range()  # ==> list, tuple, range
mapping_type = {}  # => dict
set_type = set()  # => set, frozenset
bool_type = False  # ==> bool
binary_type_1 = b""  # binery or value # ==> bytes
binary_type_2 = bytearray(b"")  # or value # ==> bytearray
binary_type_3 = memoryview(bytes(b""))  # or value # ==> # ==> memoryview

print("Value:", bool_type, " Type:", type(bool_type), " Boolean Check:", bool(bool_type))
print("Value:", numeric_type, " Type:", type(numeric_type), " Boolean Check:", bool(numeric_type))
print("Value:", decimal_type, " Type:", type(decimal_type), " Boolean Check:", bool(decimal_type))
print("Value:", text_type, " Type:", type(text_type), " Boolean Check:", bool(text_type))

print("Value:", mapping_type, " Type:", type(mapping_type), " Boolean Check:", bool(mapping_type))
print("Value:", list_type, " Type:", type(list_type), " Boolean Check:", bool(list_type))
print("Value:", tuple_type, " Type:", type(tuple_type), " Boolean Check:", bool(tuple_type))
print("Value:", binary_type_1, " Type:", type(binary_type_1), " Boolean Check:", bool(binary_type_1))
print("Value:", binary_type_2, " Type:", type(binary_type_2), " Boolean Check:", bool(binary_type_2))
print("Value:", binary_type_3, " Type:", type(binary_type_3), " Boolean Check:", bool(binary_type_3))
print()

# changeable and no data type ---------------------------------------
changeable_value = 4
print(type(changeable_value))

changeable_value = "MARK"
print(type(changeable_value))

changeable_value = True
print(type(changeable_value))
print()

# typecasting  ------------------------------------------------------
numeric_value = 1
string_value = str(numeric_value)
bool_value = bool(string_value)

print(type(numeric_value))
print(string_value)
print(bool_value)

# Naming Convention
"""
CamelCase  =>  firstLetter
PascalCase =>  FirstLetter
SnakeCase  =>  first_name
"""

# Multi value assignment
a, b, c = 1, 2, 3

# One Value to Multiple Variables
d = e = f = g = 1

# Unpacking a sequence [list, tuple, range]
w, x, y, z = [1, 2, 3, 4]
"""
package : practice
name    : practice_2_variables.py
chapter : variables
topics  : []
"""

# data_types  -------------------------------------------------------
numeric_type = 0  # ==> int
decimal_type = 0.0  # ==> float
text_type = ""  # ==> str
sequence_type = []  # [list] / {tuple} / range()  # ==> list, tuple, range
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
print("Value:", sequence_type, " Type:", type(sequence_type), " Boolean Check:", bool(sequence_type))
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

print(numeric_value)
print(string_value)
print(bool_value)

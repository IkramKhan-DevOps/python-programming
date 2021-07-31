

# FUNCTION - type1 ---------------------------------------------------------------------------------------------
def addition_1():
    num1 = 10
    num2 = 20
    result = num1 + num2
    print(
        """
        Number1: {} 
        Number2: {} 
        Result : {}
        """.format(num1, num2, result)
    )


# FUNCTION - type2 ---------------------------------------------------------------------------------------------
def addition_2(num1, num2):
    result = int(num1) + int(num2)
    print(
        """
        Number1: {} 
        Number2: {} 
        Result : {}
        """.format(num1, num2, result)
    )


# FUNCTION - type3 ---------------------------------------------------------------------------------------------
def addition_3():
    num1 = 10
    num2 = 20
    result = num1 + num2
    return result


# FUNCTION - type4 ---------------------------------------------------------------------------------------------
def addition_4(num1, num2):
    result = int(num1) + int(num2)
    return result


""" ________________________________________________________________________________________________"""
"""                                        EXTRA IN PYTHON                                          """
""" ________________________________________________________________________________________________"""


# FUNCTION: Default args => arguments/parameters => function(values) -------------------------------------------
def student_registration1(name, roll_no):
    print("Name:", name, "Roll no:", roll_no)


# FUNCTION: Keyword args => ------------------------------------------------------------------------------------
def student_registration2(name, roll_no):
    print("Name      : ", name)
    print("Roll no   : ", roll_no)
    print()


def simple_sum(num1, num2):
    print("Result:", num1+num2)


def arbitrary_sum(*args):
    result = 0
    for n in args:
        result += n
    print("Result:", result)


def student_marks(name, **marks):
    print("NAME :", name)
    print("TOTAL:", 400)
    print()

    result = 0
    for key, value in marks.items():
        result += value
        print(key, value)

    print()
    print("OBTAINED:", result)


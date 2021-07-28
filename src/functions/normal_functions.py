"""
---------------------------------------------------------------------------------------------
How to create function
2: DEFINITION
3: CALL
---------------------------------------------------------------------------------------------
ARGS   => ()  => Windows
RETURN => int => Door Exit
--------------------------------------------------------------------------------------------
1: Noo args: Noo return     =>   void name(void){}             => def name():
2: Yes args: Yes return     =>   int name(int, int){return 1}  => def name(num1, num2):return
1: Yes args: Noo return     =>   void name(int, int){}         => def name(num1, num2):
2: Noo args: Yes return     =>   int name(void){return 1}      => def name():return
--------------------------------------------------------------------------------------------
"""


def sum_nr_na():
    """
    When no inputs from outside and No result required
    :return:
    """
    num1 = 10
    num2 = 20
    print(num1 + num2)


def sum_yr_ya(num1, num2):
    """
    When inputs from outside and result required
    :param num1:
    :param num2:
    :return result:
    """
    return num1 + num2


def sum_nr_yp(num1, num2):
    """
    When inputs from outside and No result required
    :param num1:
    :param num2:
    :return:
    """
    print(num1 + num2)


def sum_yr_np():
    """
    When no inputs from outside and result required
    :return result:
    """
    num1 = 2
    num2 = 3
    return num1 + num2


def returns_values():
    return 1, 2, 3, 4, 5

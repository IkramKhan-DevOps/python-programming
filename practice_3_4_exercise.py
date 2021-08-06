"""
package : practice
chapter : Repetition control statements
topics  : []
"""

"""
   
   Ikram => CTO
   Ali   => CEO
   Sheraz=> HR
   Slaman=> Testing Officer
   Junaid=> Acting CTO
   Zahida=> Acting CEO
   
   
"""


def if_elif_else():
    """
    1. Multiple conditions
    2. check all conditions unless encounters true
    :return:
    """
    username = input("Enter team member name: ")
    if username == 'ikram':
        print("RANK: CTO")

    elif username == "ali":
        print("Rank: CEO")

    elif username == "sheraz":
        print("Rank: HR")

    elif username == "salman":
        print("Rank: TO")

    elif username == "junaid":
        print("Rank: A-CTO")

    elif username == "zahida":
        print("Rank: A-CEO")

    else:
        print("Not a member of Exarth, please visit exarth.com/about-us")


def if_if():
    """
    1. Multiple conditions
    2. check all conditions
    :return:
    """
    username = input("Enter team member name: ")
    if username == 'ikram' or username == 'junaid':
        print("RANK: CTO")

    if username == "ali" or username == 'zahida':
        print("Rank: CEO")

    if username == "sheraz":
        print("Rank: HR")

    if username == "salman":
        print("Rank: TO")

    if username == "junaid":
        print("Rank: A-CTO")

    if username == "zahida":
        print("Rank: A-CEO")



"""
   1-10 scale -> evaluation scale

   1-5  scale -> student
      1-3 scale -> programming
      4-5 scale -> framework
   6-10 scale -> developer
      6-7  scale -> Internee
      8-10 scale -> job
   
"""


def registration(marks):
    if 0 < marks < 11:  # 1-10 [marks > 0 and marks < 11]
        if marks <= 5:  # .. 0 1 2 3 4 5
            if marks <= 3:  # ... 0 1 2 3
                print("You are enrolled as a Programmer")
            else:  # 4 5
                print("You are enrolled as a Developer")
        else:  # 6 7 8 9 10 ...
            if marks <= 7:  # 6 7
                print("You are enrolled as a Internee")
            else:  # 8 9 10 ...
                print("Congrats you got the job")
    else:
        print("Please select numbers between 1-10")


""" PASS, CONTINUE, BREAK ELSE in LOOPS"""
"""
    PRIME NUMBER => number/1 = mode 0 and number/number = mode 0  => %
    18 => CHECK  =>  not-prime
    13 => CHECK  =>  prime
    7  => CHECK  =>  prime
    12 => CHECK  =>  not-prime
    15 => CHECK  =>  not-prime
    [1-15 (15%1) = 0 [15%2=NZ 15%3=NZ 15%4=NZ .....] (15%15) == 0]
"""


def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            print("Number " + str(number) + " is NOT-PRIME")
            break
    else:  # 1: When no break encounter in loop 2: loop [if]
        print("Number " + str(number) + " is PRIME")


def is_prime_while(number):
    n = 2
    while n < number:
        if number % n == 0:
            print("Number " + str(number) + " is NOT-PRIME")
            break
        n += 1
    else:  # 1: When no break encounter in loop 2: loop [if]
        print("Number " + str(number) + " is PRIME")


is_prime_while(15)
is_prime_while(4)
is_prime_while(13)

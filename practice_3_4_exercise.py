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


registration(1)
registration(2)
registration(3)
registration(4)
registration(5)
registration(6)
registration(7)
registration(8)
registration(9)
registration(10)
print()
registration(0)
registration(-1)
registration(1000)
registration(11)



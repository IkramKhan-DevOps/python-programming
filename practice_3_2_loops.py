"""
package : practice
chapter : Repetition control statements
topics  : [for-while no do-while => for = foreach]
for     : termination known
while   : un-expected
"""

# Types and uses
# FOR => for value in sequence/range:
a, b, c, d, e, f, g, h, i = list(range(2, 20, 2))


def range_loop(end, start=0, increment=1):
    _range = range(start, end, increment)
    print("LENGTH: ", len(_range))

    for number in _range:  # for(int i=0; i<10;i++)
        print(number)
    print()


def sequence_loop():
    for letter in "Junaid":
        print(letter)


# For and else in for


# while and else in while

def registration_while():
    marks = 5

    while 0 < marks < 11:
        name = input("enter marks: ")
        marks = int(input("enter marks: "))
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

# break


# continue

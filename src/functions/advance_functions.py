"""
1. Default Args
2. Non-Default first args > default args
2. Pass
3. Arbitory arguments             =>  *args
4. Arbitory keyword arguments     =>  **kwargs
"""


def addition(num1, num2):
    print(num1+num2)


def default_addition(num1=10, num2=20):
    print(num1+num2)


def authentication(password, username='admin'):
    if username == 'admin':
        print("Welcome: Admin")
    else:
        print("Welcome "+username)



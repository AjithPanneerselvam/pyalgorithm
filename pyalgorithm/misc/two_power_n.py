"""
To check whether a number is divisible by powers of 2
"""

def find(number):
    if number == 1:
        return True

    elif(not(number and number-1)):
        return True
    else:
        return False

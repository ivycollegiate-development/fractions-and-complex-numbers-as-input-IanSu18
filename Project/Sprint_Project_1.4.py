from fractions import Fraction
try:
    a = Fraction(input(("please enter a fractional number here: (ex:3/4) ")))
    print(a*4)
except ZeroDivisionError:
    print("Invalid fraction: demoninator cannot be zero")
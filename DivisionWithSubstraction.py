# This is written in Python3 language
def new_division(dividend, divisor):
    quotient = 0
    # Repetitive substraction as follows
    while dividend >= divisor:
        dividend = dividend - divisor
        quotient += 1
    remainder = dividend
    print('Quotient: ', quotient)
    print('remainder: ', remainder)


new_division(14, 3)

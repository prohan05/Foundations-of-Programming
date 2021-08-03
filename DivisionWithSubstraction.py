# This is written in Python3
def new_division(dividend, divisor):
    quotient = 0
    # Repetitive substraction as follows
    if divisor != 0:
        while dividend >= divisor:
            if divisor != 0:
                dividend = dividend - divisor
                quotient += 1
        remainder = dividend
        print('Quotient: ', quotient)
        print('remainder: ', remainder)
    else:
        print('Division is not possible')


new_division(7, 3)
new_division(14, 3)
new_division(15, 0)

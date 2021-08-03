def division(dividend, divisor):
    quotient = 0
    sign = 1
    initial_dividend = dividend
    # Division by zero
    if divisor == 0:
        print("Division not possible!")

    # Inclusion of negative numbers
    if divisor*dividend < 0:
        sign = -1
        divisor = abs(divisor)
        dividend = abs(dividend)

    # Division using repititive subtraction
    if divisor != 0:
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        print("When", initial_dividend, "is the dividend and", divisor, "is the divisor")
        print("Quotient is ", quotient*sign)
        print("Remainder is ", dividend)


division(15,2)
division(15, -2)
division(15, 0)

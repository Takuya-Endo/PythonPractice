def add(num1, num2):
    return num1 + num2


def is_even(param):
    return param % 2 == 0


def odd_or_even(num1, num2):
    number = add(num1, num2)
    if is_even(number):
        print("this additional number is even")
    else:
        print("this additional number is odd")


odd_or_even(2, 3)

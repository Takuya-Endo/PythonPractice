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

map_a = {"odd_odd": (3, 3), "odd_even": (
    3, 2), "even_odd": (2, 3), "even_even": (2, 2)}

for key, value in map_a.items():
    print(key, end=": ")
    odd_or_even(*value)

odd_or_even(num1=1, num2=3)

list_a = [dict(num1=3, num2=3), dict(num1=3, num2=2),
          dict(num1=2, num2=3), dict(num1=2, num2=2)]

for dict_element in list_a:
    odd_or_even(**dict_element)


def do_something(message="default message"):
    print(message)


do_something()
do_something("test message")
do_something(message="test message")

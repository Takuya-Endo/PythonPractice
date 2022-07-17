import math


print(123)  # 10進数
print(0b1111011)  # 2進数
print(0o173)  # 8進数
print(0x7b)  # 16進数

print(1234.5678)
print(1.2345678e3)

print(
    "1行目"
    "2行目"
    "3行目"
)
print(
    """
    1行目
    2行目
    3行目
    """
)
print(
    """\
    1行目
    2行目
    3行目\
    """
)
# SyntaxError
# print("C:\Users\home\Desktop\PythonPractice\PythonCompleteIntroduction\Chapter2\print.py")
print("C:\\Users\\home\\Desktop\\PythonPractice\\PythonCompleteIntroduction\\Chapter2\\print.py")
print(r"C:\Users\home\Desktop\PythonPractice\PythonCompleteIntroduction\Chapter2\print.py")

print(int(1.2))
print(int(1.8))
print(int(-1.2))
print(int(-1.8))
print(float(1))
print(float(-1))
print(math.floor(1.2))
print(math.floor(1.8))
print(math.floor(-1.2))
print(math.floor(-1.8))
print(math.ceil(1.2))
print(math.ceil(1.8))
print(math.ceil(-1.2))
print(math.ceil(-1.8))

print(1 < 2 and 2 < 3)
print(1 < 2 < 3)
print(bool("test"))
print(bool(""))
print(bool(1))
print(bool(0))
print(bool("False"))
print(bool(False))

string_a = "StringA"
string_b = "StringB"
string_c = string_a

print(string_a)
print(string_c)

print(string_a == string_b)
print(string_a is string_b)
print(string_a == string_c)
print(string_a is string_c)

print(id(string_a))
print(id(string_b))
print(id(string_c))

string_a = "StringC"  # 文字列はimmutableオブジェクトのため参照も書き換わる
print(string_a)
print(string_c)

print(id(string_a))
print(id(string_b))
print(id(string_c))

print("A" + "B" + "C")
print(1 + 2 + 3)
print("A" + "B" + "C")
print("A" + str(2) + "C")

print("A" < "B")
print("A" * 5)

print("ABCDE"[1])
print("ABCDE"[-2])
print("ABCDE"[1:4])
print("ABCDE"[:2] + "C" + "ABCDE"[-2:])
print("ABCDE"[0:5:2])
print("ABCDE"[::-1])

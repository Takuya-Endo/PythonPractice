for i in range(5):
    print(i)

for i in range(5):
    print(i, end=", ")

print()
print("Python:", end=" ")
print(len("Python"), end="文字")
print()

for i in range(5):
    print(i, end="")
    print(", ", end="")

print()

for i in range(5):
    print(i, end="")
print(", ", end="")

print()

# Ctrl+K → Ctrl+C でコメントアウト
"""
複数行のコメントアウトは無し
引用符を三重にして代用可
"""

# pycodestyle print.py ←pep8に沿っているか
# autopep8 -i print.py ←pep8に沿った変更を表示
# autopep8 -i print.py ←pep8に沿った変更で上書き

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

print(1 < 2 and 2 < 3)
print(1 < 2 < 3)
print(bool("test"))
print(bool(""))
print(bool(1))
print(bool(0))
print(bool("False"))
print(bool(False))

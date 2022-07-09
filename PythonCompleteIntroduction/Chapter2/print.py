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

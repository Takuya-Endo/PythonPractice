
# 参照ドキュメント
# https://docs.python.org/ja/3/


# コマンドプロンプトでpyコマンドで>>>がでるので、一行ずつコーディングしていく。
# 終了は、Ctrl+Zかquit()かexit()。
# if文等は>>>の後に...が出るが、Tabでインデントを正しくしておかないとエラー。

# 入力予定のコードを全て.pyファイルに記述しておき、
# py ファイル名.pyで、コマンドプロンプトで実行することも可能。
# また、.batファイルにpy ファイル名.pyを記述しておくことでより便利に。

numA = 2
numB = 3
numC = 4
print(2 + 3)

strA = "文字列A"
strB = "文字列B"
print(strA + strB)

array = [0, 1, 2, 3, 5]
print(array)
print(array[0])

if numA == 2:
  print("OK")
elif numA == 3:
  print("NG")
else:
  print("NG")

if numB == 2:
  print("NG")
elif numB == 3:
  print("OK")
else:
  print("NG")

if numC == 2:
  print("NG")
elif numC == 3:
  print("NG")
else:
  print("OK")

for number in array:
  print(number)

# 関数の定義→def
def printTest():
  print("TestMethod")

def returnTest():
  return "TestMethod"

def printNumber(number):
  print(number)

printTest()
print(returnTest())
printNumber(100)

import FibonacciNumbersModule
FibonacciNumbersModule.fib(1000)
FibonacciNumbersModule.fib2(100)
FibonacciNumbersModule.__name__
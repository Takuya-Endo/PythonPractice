str = "A"
# str = "B"
# str = "C"
if str == "A":
    print("string is A")
elif str == "B":
    print("string is B")
else:
    print("string is other")

sex = "MAN"
# sex = "WOMAN"
print("SEX is MAN") if sex == "MAN" else print("SEX is WOMAN")  # 三項演算子

list_a = list("ABCDE")
for element_a in list_a:
    print(element_a, end=" ")
    for str in "abcde":
        print(str, end=", ")
    print()

map = dict(
    ja="Japanese", en="English", fr="French"
)
for element in map.keys():
    print(element, end=", ")
print()
for element in map.values():
    print(element, end=", ")
print()
for element in map.items():
    print(element, end=", ")
print()
for key_element, value_element in map.items():
    print(key_element, value_element, end=", ")
print()

for num in range(5, 21, 5):
    print(num, end=", ")
print()

map_a = {}
for key, value in enumerate(list_a):
    print(key, value)
    map_a[key] = value
print(map_a)

input_value = "y"
while input_value == "y":
    input_value = input("continue? y/n: ")

num = 0
while True:
    num += 1
    if num == 10:
        break
    print(num)

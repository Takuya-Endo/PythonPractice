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

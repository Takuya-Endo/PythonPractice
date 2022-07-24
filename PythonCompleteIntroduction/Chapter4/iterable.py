list_a = ["A", "B", "C", "D", "E"]
print(list_a, id(list_a))
list_a = list("ABCDE")
print(list_a, id(list_a))

print(list_a[1])
print(list_a[-2])
print(list_a[1:4])
print(list_a[::2])

list_b = list_a
print(id(list_a))
print(id(list_b))
list_b = list_a[:]
print(id(list_b))
list_b = list_a.copy()
print(id(list_b))

list_b = list_b[:4]
list_b.append("E")
print(list_b)
list_b = list_b[:3]
list_b += ["D", "E"]
print(list_b)
list_b = list_b[:3]
list_b += list("DE")
print(list_b)

list_b = list_b[:3]
list_b.extend(["D", "E"])
print(list_b)
list_b = list_b[:3]
list_b.extend(list("DE"))
print(list_b)
list_b = list_b[:3]
list_b[len(list_b):] = ["D", "E"]
print(list_b)
list_b = list_b[:3]
list_b[len(list_b):] = list("DE")
print(list_b)

del list_b[4]
print(list_b)
list_b.pop(3)
print(list_b)
list_b.remove("C")
print(list_b)
list_b += list("CDE")
print(list_b)
del list_b[2:3]
print(list_b)
list_b.insert(2, "C")
print(list_b)
list_b[2:3] = []
print(list_b)
list_b[1:2] += list("C")
print(list_b)

string_b = ", ".join(list_b)
print(string_b)
list_c = string_b.split(",")
print(list_c)

print(len(list_c))
print(list_c*3)
print(list_c*0)

list_d = list("AECDB")
print(list_d)
list_d.sort()
print(list_d)
list_d.sort(reverse=True)
print(list_d)
print(max(list_d))
print(min(list_d))

tuple_a = ("A", "B", "C", "D", "E")
print(tuple_a)
tuple_b = tuple_a[1:4]
print(tuple_b)
tuple_c = "A",
print(tuple_c)
tuple_d = tuple("A")
print(tuple_d)

a = tuple_a
print(a)
a, *x = tuple_a
print(a)
*x, e = tuple_a
print(e)
x, b, *x = tuple_a
print(b)
a, *x, e = tuple_a
print(a, e)

strings = "ABCDE"
list_e = [tuple(strings), ("A",), list(strings), strings, tuple(strings)]
print(list_e)

set_a = {"A", "B", "C", "D", "E"}
print(set_a)
list_a = list()
set_a = set()
print(list_a, set_a)
set_a = set("ABCDE")
print(set_a)
set_a = set("ABCDEABCDEABCDE")
print(set_a)

print("A" in set_a)
print("F" not in set_a)
login_info = {
    ("admin", "p@ssw0rd"), ("guest", "pass"), ("user", "myPass")
}
login = ("admin", "password")
print(login in login_info)
login = ("admin", "p@ssw0rd")
print(login in login_info)

set_a.add("FGH")
print(set_a)
# set_a.remove("F")
set_a.discard("F")
print(set_a)
set_a.remove("FGH")
set_a.discard("FGH")
print(set_a)
set_a |= set("FGHIJ")
print(set_a)
set_a.remove("F")
set_a.discard("G")
set_a -= {"H", "I", "J"}
print(set_a)

set_b = set("python")
set_c = set("JavaScript")
print(set_b)
print(set_c)
print(set_b | set_c)  # 和集合
print(set_b & set_c)  # 積集合
print(set_b - set_c)  # 差集合
print(set_b ^ set_c)  # 対称差

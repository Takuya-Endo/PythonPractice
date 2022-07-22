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

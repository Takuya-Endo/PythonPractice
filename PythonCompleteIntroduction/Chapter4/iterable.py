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

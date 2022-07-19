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

x = 1.5
y = -1

print(abs(x))
print(abs(y))

print(abs(6+8j))

z = y
print(id(z), id(y))


l1 = [1,2,3,4]
l2 = l1

l2[0] = 1234

print(l1)
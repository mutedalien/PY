import sys

a = 29, 345.5, 'hello', True, "world!"

# print(sys.getsizeof(a))
# print(sys.getsizeof(a[0]))
# print(type(a))
#  => immutable
# a[0] = 'hi'
# print(a)

# print(dir(a))
# print(a.index('hello'))

b = 'go'
c = 15
print(b, c)

b, c = c, b

print(b, c)

# print(help(list))

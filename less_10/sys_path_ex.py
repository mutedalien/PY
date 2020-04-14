# Мы можем импортировать
import math
# Но не можем импортировать наш модуль например на диска C:
# import mymodule

# Как питон находит модули?
import sys

print (sys.path)
print(type(sys.path))

for p in sys.path:
    print(p)
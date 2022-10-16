import os
os.system('cls' if os.name == 'nt' else 'clear')
import mrtxee
mrtxee.print_fancy('CONTROL STRUCTURES')

print('''

МОДУЛИ
подключение внешний модулей (библиотек)
import random
import mrtxee
for i in range(5):
    value = random.randint(1, 6)
    print(value)
mrtxee.print_fancy(\'CONTROL STRUCTURES\')

There is another kind of import that can be used if you only need certain functions from a module. 
from math import pi, sqrt
можно импортировать с кастомным неймингом
from math import sqrt as square_root
print(square_root(100))


ФУНКЦИИ
def my_func(a,b,c):
    print("spam")
    print("spam")
    return(a+b)
my_func(1,2,3)


УСЛОВНЫЙ ОПЕРАТОР
if [smth] :
    ...
elif [smth] :
    ...
else:
    ...

ОПЕРАТОР ДИАПАЗОНА
range(a, [b, [step]])

ОПЕРАТОРЫ ЦИКЛА for, while
for i IN range(1,3):
    [smth]

while i<100:
    i += 1
    #countinue
    #break

БУЛЕВА ЛОГИКА
Операторы сравнения (==,>=,<...) имеют более высокий приоритет or, xor, and
print(False == False or True)
True
print(False == (False or True))
False
print((False == False) or True)
True

''')
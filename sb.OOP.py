import os
os.system('cls' if os.name == 'nt' else 'clear')
import mrtxee

mrtxee.print_fancy('OOP: CLASS DECLARATION',
                    'конструктор класса __init__')
#все методы класса должны содержать параметр self,
#который не передается в явном виде
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + str(self.level) + ")")

#your code goes here
new_player = Player('Tony', 12)
new_player.intro()


mrtxee.print_fancy('OOP: Inheritance, наследование',
                    'class My_Class(Parent_Class):')
class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()

mrtxee.print_fancy('OOP: Inheritance, super()',
                    'обращение к родительскому классу')
class A:
    def spam(self):
        print('1 - parent')
class B(A):
    def spam(self):
        print('2 - son')
        super().spam()
B().spam()

mrtxee.print_fancy('OOP: MAGIC METHODS :: __sub__, __mul__, ... ',
                    'суммирование объектов')
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self):
        return self.x
    def __getitem__(self, index=1):
        if 1==index:
            return self.x
        else:
            return self.y
    def __len__(self):
        return self.x+self.y
    def __gt__(self, other):
            return self.area() > other.area()
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)
    # статические методы можено вызывать без экземпляра класса
    @staticmethod
    def area_for_any(h,w):
        return h*w


'''
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for | 
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >= 
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in 
__call__ for calling objects as functions
__str__...
'''
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(f'result.x \t {result.x}')
print(f'second[2] \t {second[2]}')
print(f'len(second) \t {len(second)}')
print(f'first > first \t {first > first}')
#mrtxee.explore_obj(first)
square = Vector2D.new_square(3)
print(f'square .x, .y \t {square.x}, {square.y}' )
print(f'static_method_call \t {Vector2D.area_for_any(12, 17)}')

mrtxee.print_fancy('OOP: ENCAPSULATION (data hiding) ',
                    'Инкапсуляция (сокрытие реализации)')
class Queue:
    def __init__(self, contents):
        # маркируем параметры скрытым
        self._hiddenlist = list(contents)
        # делаем параметр private
        self.__privatelist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
#print(queue.__privatelist) # сбой в работе транслятора
mrtxee.print_fancy('OOP: принципы',
                    'Инкапсуляция (сокрытие реализации), Наследование, Полиморфизм (разные формы одной сущности)')
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = "Sw0rdf1sh!"#input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")
    #@pineapple_allowed.getter

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)




mrtxee.print_fancy('OOP: принципы',
                    'Инкапсуляция (сокрытие реализации), Наследование, Полиморфизм (разные формы одной сущности)')
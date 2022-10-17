import os
os.system('cls' if os.name == 'nt' else 'clear')
import mrtxee

mrtxee.print_fancy("= = = Functional Programming = = =")
#ДЕКОРАТОРЫ
# - это Функции, которые модифицируют другие функции.
mrtxee.print_fancy('FP: sample of DECORATORs, 1',
                    'с сохранением имени декорируемой функции')
def decor(func):
    def wrap1(num):
        print('***')
        func(num)
        print('***')
        print('END OF PAGE')
    return wrap1
@decor # приклеивание декора к методу
def invoice(num):
    print("INVOICE #" +num)
invoice('100')

mrtxee.print_fancy('FP: sample of DECORATORs, 2',
                    'создаем новую функцию с учетом декорируемой')
def decor_it(func, s='ss2'):
    def wrap():
        print("============")
        func(s)
        print("============")
    return wrap
def any_f(s='11'):
    print("Hello world!"+s)
#описываем метод, который будет декорировать сущетсвующий
decorated_f = decor_it(any_f)
decorated_f()


#ГЕНЕРАТОРЫ данных yield
mrtxee.print_fancy('FP: sample of GENERATORs, 1',
                    'получаем набор данный из сторонней функции в цикле при помомщи yield')
def isPrime(x): # проверка простое число или нет
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True
def primeGenerator(a, b):
    for i in range(a,b):
        if isPrime(i):
            yield i    
f = 1#int(input())
t = 100#int(input())
generated_list = list(primeGenerator(f, t))
print(generated_list)

## ЛЯМБДА-функции - анонимные в функции, eg.
mrtxee.print_fancy('FP: sample of LAMBDAs, 1',
                    'получаем рез-т при пом. lambda - анонимной функции')
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(19))
#lambda
print((lambda x: x**2 + 5*x + 4) (19))
#0) отфильтровать все четные числа при помощи filter(), lambda
mrtxee.print_fancy('FP: sample of LAMBDAs, 2',
                    'фильтруем коллекцию в 1 строку при пом. lambda, filter()')
nums = [1, 2, 8, 3, 7]
res = list( filter( lambda x: x%2==0, nums) )
print(res)
mrtxee.print_fancy('FP: sample of LAMBDAs, 3',
                    'меняем данные в коллекции в 1 строку при пом. lambda, map()')
#1) #map() - применить метод к каждому значению списка
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = 30#int(input())
salaries = list ( map(lambda num: num + bonus, salaries) )
print(salaries)
mrtxee.print_fancy('FP: *args and **kwargs',
                    'переменные, аргументы функции, позволяют загрузить любое число перменных в список, словарь соответсвенно')
mrtxee.print_fancy('FP: Recursion',
                    'рекурсии, база рекурсии, рекурсивный вызов')


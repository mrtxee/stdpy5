import os
os.system('cls' if os.name == 'nt' else 'clear')
import mrtxee
mrtxee.print_fancy('CT: COLLECTION TYPES')

mrtxee.print_fancy('CT: LISTs, List Operators:',
                    '= reassigne, +, *, in')
words = ["Hello", "world", "!"]
print(words[0])
#вложенные списки - ок
things = ["string", 0, [1, 2, 3], 4.56]
things[1]='X'
print(things)
#строка - это тоже список
print("Hello world!"[6])
print('привет как дела??')


mrtxee.print_fancy('CT: LISTs, List functions:',
                    '.append(), len(), .insert(index, item), .index(item)...')
'''
There are a few more useful functions and methods for lists.
max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(item): Returns a count of how many times an item occurs in a list
list.remove(item): Removes an object from a list
list.reverse(): Reverses items in a list. 
'''
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print(f'letters.index(\'r\') {letters.index("r")}')
print(f'letters.insert(3,\'d\') {letters.insert(3,"d")}')
print(f'letters.append(\'я\') {letters.append("я")}')
print(letters)

mrtxee.print_fancy('CT: DICTIONARIes, словари',
                    'methods')
mrtxee.print_fancy('CT: SETs, множества',
                    'Прикольные операторы сочетания коллекций')
# Прикольные операторы сочетания множеств 
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second) #union
print(first & second) #intersection
print(first - second) #difference
print(first ^ second) #symmetric difference
third = first ^ second
print(third)
mrtxee.print_fancy('CT: TUPLEs, кортежи',
                    'множества')
mrtxee.print_fancy('CT: sample of LIST COMPREHENSION, 1 (генератор коллекции)',
                    'считаем кол-во вхождение в 1 строку')
text = 'hello'#input()
print ( text )
result = {i:text.count(i) for i in text}
print ( 'число вхождений: '+str(result) )
# a list comprehension ~ генератор списка / можножества / кортежа

mrtxee.print_fancy('CT: sample of LIST COMPREHENSION, 1 (генератор коллекции)',
                    'считаем кол-во вхождений в списке в 1 строку')
word = 'awesome'
word_list = list(word)
vowels_list = list('aeiou')
print( word_list )
mrtxee.print_fancy('CT: sample of LIST COMPREHENSION, 1 (генератор списка)',
                    'удалить глассные в 1 строку')
result = [i for i in word_list if i not in vowels_list]
print('a = '+str(result))
#2)
people = [{
  "first_name": "Василий",
  "last_name": "Марков",
  "birthday": "9/25/1984"
}, {
  "first_name": "Регина",
  "last_name": "Павленко",
  "birthday": "8/21/1995"
}]
birthdays = [
  person[term]
  for person in people
  for term in person
  if term == "birthday"
]
print(birthdays)

# синтаксический сахар
# a list comprehension ~ генератор списка
cubes = [i**3 for i in range(5)] # [0, 1, 8, 27, 64]
print(cubes)

import os
os.system('cls' if os.name == 'nt' else 'clear')
#import this
import mrtxee
mrtxee.print_fancy('= = = EXEPTIONS = = =')

mrtxee.print_fancy('E: try ... except',
                    'поймать исключение по типу либо без')
try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")
except (ValueError, TypeError):
    print("Value or type error")
except: # любое исключение
    print("Any other Error occurred")
else:
    print("There was no ant exception!")
finally:
    print("This code will run no matter what")

mrtxee.print_fancy('E: Exception Raise',
                    'вызвать исключение')
num = 102
num = 99
if num > 100:
  raise ValueError

mrtxee.print_fancy('E: Exception Raise',
                    'вызвать исключение с кастомным текстом')
#num = 102
num = 99
if num > 100:
  raise ValueError("Парень там ввел 102!")

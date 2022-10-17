import os
os.system('cls' if os.name == 'nt' else 'clear')
#import this
import mrtxee
mrtxee.print_fancy('= = = FILES = = =')
fname = "filename.txt"

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])
'''
mrtxee.print_fancy('F: FILE, read, write',
                    'прочитаю файл, либо создам новый и прочитаю со второй попытки')
try:
    f = open(fname, "r")
    print(f.read())
    #второй ввариант - получить список строк
    #lines = file.readlines()
except FileNotFoundError:
    print("не удалось открыть файл "+fname)
    print("создаю новый")
    f = open(fname, "w")
    f.write("This has been written to a file start")    
except:
    print("сбой при работе с файлом")
finally:
    f.close()

mrtxee.print_fancy('F: FILE, append',
                    'дозапись в конец файла')
file = open(fname, "a")
bytes_written = file.write("\nThis has been written WITH APPEND to a file")
print(f'bytes_written: {bytes_written}')
file.close()

mrtxee.print_fancy('F: FILE, read, ???',
                    'с автоматической обработкой исключений и авто. закрытием файл')
with open(fname) as f:
    print(f.read())
    f.close()
'''
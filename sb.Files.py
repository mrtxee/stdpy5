import os
os.system('cls' if os.name == 'nt' else 'clear')
#import this
import mrtxee
mrtxee.print_fancy('= = = FILES = = =')
fname = "filename.txt"


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
'''
mrtxee.print_fancy('F: FILE, read, ???',
                    'с автоматической обработкой исключений и авто. закрытием файл')
with open(fname) as f:
    print(f.read())
    f.close()

'''
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "w+" ???
Sending "a" means append mode, for adding new content to the end of the file.
Adding "b" to a mode opens it in binary mode, which is used for non-text files
'''
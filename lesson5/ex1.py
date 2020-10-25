''' Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

with  open("lesson5/ex1.txt", 'w') as f:
    while True:
        string = input("ex1.txt -> ") + ' \n'
        f.writelines(string)
        if string  == ' \n':
            print('End of File')
            break
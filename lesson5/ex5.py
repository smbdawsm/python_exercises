'''
Создать (программно) текстовый файл, записать
в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randint

def summa(string):
    summ = 0
    for el in string.split():
        new_el = el
        for letter in el:   
            if letter == '[' or letter == ']' or letter ==',':
                new_el = new_el.replace(letter, '')
            else: pass
        summ += int(new_el)
    return summ

with open('lesson5/ex5.txt', 'w') as f:
    f.writelines(str([randint(1,150) for el in range(1,50)]))

with open('lesson5/ex5.txt', 'r') as f:
    while True:
        content = f.readline()
        if content == '':
            break
        print(summa(content))

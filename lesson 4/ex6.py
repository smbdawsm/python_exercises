''' Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
 что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем
 цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
 '''

from random import randint
from itertools import count
from itertools import cycle
n = 1
m = int(input('Choose begin count'))
try:
    for el in count(m):
        if m == 15:
            a = int(input('Хотите бесконечный цикл? '))
        else:
            print(el) 
            m += 1
except ValueError:
    print('Ну уж нет')       


random_list = [chr(randint(97,123)) for el in range(1,6)]
print(random_list)
try:
    for el in cycle(random_list):
        if n == 15:
            print(el)
            a = int(input('Может хватит уже? '))
        else:
            print(el)
            n += 1
except ValueError:
    print('То-то же...')
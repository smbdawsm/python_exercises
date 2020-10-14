'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
''' Если не позиционными'''
def my_func(*args):
    print(f'sum = {sum(args) - min(args)}')

my_func(3, 2, 1)

def my_func2(a,b,c):
    print(f'sum = {a+b+c-min(a,b,c)}')
try:
    my_func2(int(input('a?  ')), int(input('b?  ')), int(input('c?  ')))
except ValueError:
    print('Некорректный ввод')
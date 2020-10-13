'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
''' Если не позиционными
def my_func(*args):
    print(f'sum = {sum(args) - min(args)}')

my_func(3, 2, 1)
'''
def my_func(a,b,c):
    print(f'{a+b+c-min(a,b,c)}')

my_func(3,2,1)

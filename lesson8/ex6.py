'''
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''

class MyOwnExeption(Exception):

    def __init__(self, text):
        self.text = text

    @staticmethod
    def valid_number(n):
        if n.isdigit():
            return True
        else: return False


'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, 
например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''

class MyOwnException(Exception):

    def __init__(self, text):
        self.text = text

    @staticmethod
    def type_of_string(string):
        if string.isdigit():
            return True

def input_string(string):
    for_answer_string = []
    for el in string.split():
        if MyOwnException.type_of_string(el):
            for_answer_string.append(el)
        elif el == 'stop':
            return 'stop'
        else: raise MyOwnException('Вводите только цифры')
    print(for_answer_string)
    return True


def mainloop():
    while True:
        try:
            if input_string(input('...: ?')) == 'stop':
                break
        except MyOwnException as err:
            print(err)
mainloop()
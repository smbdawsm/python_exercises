'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в 
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class OwnExeption(Exception):

    def __init__(self, text):
        self.text = text


while True:
    try:
        a = int(input('Enter A: ')) 
        b = int(input('Enter B: '))
        if b == 0: 
            raise OwnExeption('this is a division by zero')  
        print(f'Answer is {a/b} \nPress Enter to continue, or type "exit" to stop the program') 
    except ValueError as err:
        print('Invalid input', err)
    except OwnExeption as err:
        print(err)
    finally:
        if input() == 'exit':
            break
    
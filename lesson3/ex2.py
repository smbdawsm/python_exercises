'''Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. Функция должна принимать 
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

def personal(**kwargs):
    print(kwargs)


personal(name='Nikolay',lastname='Nikishev',bday='22.10.1991',city='Novosibirsk',email='nikolay.nikishev@icloud.com',phone='89830510328')

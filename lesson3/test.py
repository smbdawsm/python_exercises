persons = []


def addinfo(name='', surname='', year_of_birth=None, city='', email='', phone='', dictionary=persons):
    """
    Фунцкия которая записывает введенные данные в шаблон словаря, затем вставляет шаблон в список и возвращает его.

    Первые параметры вводятся пользователем вручную.
    Последний аргумент вставляется по умолчанию.
    dictionary - список со словарями.
    """
    template = {
        "Имя": name,
        "Фамилия": surname,
        "Год рождения": year_of_birth,
        "Город": city,
        "email": email,
        "Номер": phone,
    }
    dictionary.append(template)
    return dictionary


# test = [
#     {
#         "Имя": "name",
#         "Фамилия": "surname",
#         "Год рождения": "yearOfBirth",
#         "Город": "city",
#         "email": "email",
#         "Номер": "phone",
#     },
# ]
# printInfo(test) # Тестовая запись для проверки функции

def printinfo(info):
    """
    Функция принимает в себя список с записями и выводит отдельные записи в двух варициях:

    1. Строкой
    2. Столбцом
    """
    tab = input("Вывести строкой [y/n]? ")
    i = 0
    for card in info:
        i += 1
        print(f"\n{'*'*10}\nЗапись №{i} \n{'*'*10}\n")
        for key, value in card.items():

            print(f"{key}: {value}", end="\n") if tab.lower() != "y" else print(f"{key}: {value}", end="\t||\t")

#


while True:
    print("""
    
Добро пожаловать в меню!

Для того чтобы записать данные человека укажите [a]*.
Для того чтобы вывести все данные, то укажите [p]*.
Для того чтобы выйти, укажите [x]*.
*элементы указаны на латинице
    """)
    choose = input("Ваш выбор: ")
    if choose.lower() == "a":
        addinfo(
            name=input("Ваше Имя: "),
            surname=input("Ваша Фамилия: "),
            year_of_birth=int(input("Ваш год рождения: ")),
            city=input("Город проживания: "),
            email=input("Электронная почта: "),
            phone=input("Номер телефона: ")
        )
    elif choose.lower() == "p":
        printinfo(persons)
    elif choose.lower() == "x":
        break
    else:
        print("К сожалению такого варианта не предусмотрено.")
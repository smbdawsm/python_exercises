'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца 
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class Date():

    def __init__(self, string):
        self.date = string

    @classmethod
    def parse_string(cls, string):
        parselist = string.split('-')
        day, month, year = int(parselist[0]), int(parselist[1]), int(parselist[2])
        if Date.validation_string(day,month,year):
            return f'A day {day}, and a month  {month}, of year {year}'
        else:  return f'Date {day, month, year} is not valid'


    @staticmethod
    def validation_string(day,month,year):
        if day in range(1,32) and month in range(1,13) and year in range(2000, 2021):
            return True 

may9 = Date('29-5-1995')
print(may9.parse_string('29-5-1995'))
print(Date.parse_string('03-12-2012'))
try:
    print(Date.parse_string(input('Enter the date in format "day-month-year", range of years 2000-2021: ')))
except ValueError as err:
    print(err, 'Invalid data format')
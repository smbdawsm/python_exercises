'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники 
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках 
реализовать параметры, уникальные для каждого типа оргтехники. 
'''
from itertools import cycle
from abc import abstractmethod, ABC
from ex6 import MyOwnExeption

class Warehouse(ABC):

    Organization_Units = {
    'Callcenter' : [],
    'IT': [],
    'Manager': []
    }

    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def show_org_equipment():
        return f"\n Units in Callcentre: {len(__class__.Organization_Units['Callcenter'])} \n Units in IT: {len(__class__.Organization_Units['IT'])} \n Units in Manager: {len(__class__.Organization_Units['Manager'])}"


class Office_equipment(Warehouse):



    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @staticmethod
    def show_all():
        return f'Printers count {Printer.counter}, Scanner count {Scanner.counter}, Copier count {Copier.counter}'

    '''
    @abstractmethod
    def income(self, n):
        pass
    '''


class Printer(Office_equipment):
    
    counter = 0
    addprint = []
    
    def __init__(self, name = 'Printer', quantity = 1):
        super().__init__(name, quantity)
        self.__class__.counter += 1


    @staticmethod
    def income(n):
        __class__.addprint = [Printer(input('Enter the name of Printer please: ')) for i in range(n)]
        return f'{n} Rows success!'

    @staticmethod
    def removeFromWH(key, n):
        try:
            if n < (len(__class__.addprint)):
                for i in range(n):
                    Warehouse.Organization_Units[key].append(__class__.addprint.pop(0))
                __class__.counter -= n
                return f'{n} Rows success!'
            else: 
                raise MyOwnExeption(f'\n We have not {n} printers in WH\n ')
        except MyOwnExeption as err:
            print(err)
            return False


class Scanner(Office_equipment):
    
    counter = 0
    addscan = []

    def __init__(self, name = 'Scanner', quantity = 1):
        super().__init__(name, quantity)
        self.__class__.counter += 1

    @staticmethod
    def income(n):
        __class__.addscan = [Scanner(input('Enter the name of Scanner please: ')) for i in range(n)]
        return f'{n} Rows success!'
    
    @staticmethod
    def removeFromWH(key, n):
        try:
            if n < (len(__class__.addscan)):
                for i in range(n):
                    Warehouse.Organization_Units[key].append(__class__.addscan.pop(0))
                __class__.counter -= n
                return f'{n} Rows success!'
            else: 
                raise MyOwnExeption(f'\n We have not {n} scanners in WH\n ')
        except MyOwnExeption as err:
            print(err)
            return False


class Copier(Office_equipment): 
    
    counter = 0
    addcopy = []

    def __init__(self, name = 'Copier', quantity = 1):
        super().__init__(name, quantity)
        self.__class__.counter += 1
    
    @staticmethod
    def income(n):
        __class__.addcopy = [Copier(input('Enter the name of Copier please: ')) for i in range(n)]
        return f'{n} Rows success!'

    @staticmethod
    def removeFromWH(key, n):
        try:
            if n < (len(__class__.addcopy)):
                for i in range(n):
                    Warehouse.Organization_Units[key].append(__class__.addcopy.pop(0))
                __class__.counter -= n
                return f'{n} Rows success!'
            else: 
                raise MyOwnExeption(f'\n We have not {n} copiers in WH\n ')
        except MyOwnExeption as err:
            print(err)
            return False

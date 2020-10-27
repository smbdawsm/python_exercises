'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который 
должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости с
выше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car():

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('ARONDONDON')

    def stop(self):
        print('Stop the Car')

    def turn(self, direction):
        print(f'Car turn {direction}')

    def show_speed(self, speed):
        return (f'{self.name} is mooving with speed {speed} km/h')

class TownCar(Car):
    
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed)

    def show_speed(self, speed):
        try:
            if int(speed) > 60:
                return (f'Вы превысили скорость на {int(speed) - 60}')
            else: return (f'{self.name} is mooving with speed {speed} km/h')
        except ValueError as err:
            print(err)
            
class WorkCar(Car):
    
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed)

    def show_speed(self, speed):
        try:
            if int(speed) > 40:
                return (f'Вы превысили скорость на {int(speed) - 40}')
            else: return (f'{self.name} is mooving with speed {speed} km/h')
        except ValueError as err:
            print(err)

class SportCar(Car):
    
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed)
        super().show_speed(self)
        
       

class PoliceCar(Car):
    
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed)
    

pC = PoliceCar('Lada Granta', 'white', 80)
sC = SportCar('Toyota Supra', 'pink', 140)
wC = WorkCar('Mitsubishi Delica', 'black', 60)
tC = TownCar('Honda Civic', 'grey', 80)

print(wC.show_speed(39))
print(tC.show_speed(120))
pC.go()
sC.stop()
print(sC.show_speed(180))

'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата
'''

class Complex():

    def __init__(self, real, notreal):
        self.real = real
        self.notreal = notreal

    def __str__(self):
        return f'{self.real} + {self.notreal}j'

    def __add__(self, other):
        return f'{(self.real + other.real)} + {self.notreal + other.notreal}j'
    
    def __mul__(self, other):
        return f'{(self.real*other.real - self.notreal*other.notreal)} + {(self.real*other.notreal + self.notreal*other.real)}j'


a = Complex(2,1)
b = Complex(3,4)

print(a + b)
print(a * b)
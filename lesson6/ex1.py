'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 
2 секунды, третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно 
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
 создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить 
соответствующее сообщение и завершать скрипт.
'''
import asyncio
import time


class TrafficLight():

    def __init__(self):
        self.color = 'red'

    async def running(self):
        self.color = 'red'
        await self.output(7, self.color)
        self.color = 'yellow'
        await self.output(2, self.color)
        self.color = 'green'
        await self.output(5, self.color)

    async def output(self, sleep, text):
        while sleep > 0:
            await asyncio.sleep(1)
            print(f'{text} light, remain {sleep} seconds')
            sleep -= 1

a = TrafficLight()

while True: 
    asyncio.run(a.running())

        
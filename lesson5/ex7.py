'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные 
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
 со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''

import json

def diff_profit(dohod, izderjka):
    return int(dohod) - int(izderjka)

ANSWER ={}
with open('lesson5/ex7.txt', 'r', encoding='utf-8') as f:
    n = 0
    common_profit = 0
    while True:
        content = f.readline()
        if content == '':
            break
        parse_string = content.split()
        print(parse_string)
        dohod = parse_string[2]
        izderjka = parse_string[3]
        if diff_profit(dohod, izderjka) > 0:
            n += 1
            common_profit += diff_profit(dohod, izderjka)
        ANSWER.setdefault(parse_string[0], diff_profit(dohod, izderjka))

average_profit = common_profit / n
answer_list = [ANSWER, {"average_profit":average_profit}]
print(answer_list)

with open('lesson5/ex7.json', 'w') as f:
    f.write(json.dumps(answer_list, sort_keys=True, indent=4))


'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''
with open('lesson5/ex3.txt', 'r') as f:
    n = 0
    for_diff_summ = 0
    while True:
        base = {}
        content = f.readline()
        parsed_string = content.split()
        if content == '':
            break
        elif int(parsed_string[1]) < 20000:
            print(parsed_string[0])
        n += 1
        for_diff_summ += int(parsed_string[1])
    print(f'Средняя зарплата сотрудников {for_diff_summ/n}')

    
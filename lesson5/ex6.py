'''
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) 

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
def summa(string):
    summ = 0
    for el in string.split():
        new_el = 0
        hours = '0'
        for letter in el:   
            if letter.isdigit():
                hours += letter
            else: pass
        new_el = int(hours)
        summ += int(new_el)
    return summ
def clear_word(word):
    good_word = ''
    for letter in word:
        if letter != ':':
            good_word += letter
    return good_word
ANSWER = {}

with open('lesson5/ex6.txt', 'r', encoding='utf-8') as f:
    while True:
        content = f.readline()
        if content == '':
            break
        parse_string = content.split()
        ANSWER.setdefault(clear_word(parse_string[0]), summa(content))

print(ANSWER)
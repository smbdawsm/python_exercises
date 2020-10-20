'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('lesson5/ex4in.txt', 'r') as f:
    to_write_list = []
    while True:
        content = f.readline()
        if content == '':
            break
        else:
            parsed_string = content.split()
            for k,v in dictionary.items():
                if parsed_string[0] == k:
                    string_to_new_file = v + ' - ' + parsed_string[2] + '\n'
                    to_write_list.append(string_to_new_file)

with open('lesson5/ex4out.txt', 'w', encoding='utf-8') as f:
    for el in to_write_list:
        f.writelines(el)

                
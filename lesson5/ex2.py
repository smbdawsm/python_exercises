'''
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''

with open('lesson5/ex2.txt', 'r') as f:
    i = 0
    while True:
        n = 0
        content = f.readline()
        print(content)
        i += 1
        for el in content.split():
            if el.isdigit() == False:
                n += 1
            else: pass
        if content == '':
            print(f'End of File, strings - {i}')
            break
        else: print(f'words at string - {n}')
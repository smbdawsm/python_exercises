print('-'*40)
print('Welcome to warehouse')
print('-'*40)
i = 1
choose = ''
entree = {"name":  "" , "price": "", "quantity": ""}
db = {}
new_db = db.copy()
stat = {"name": [], "price": [], "quantity": []} 
# Функция счетчика записей в словаре, для дозаписи
def Icalculate():
    a = 1
    for k in db:
        a += 1
    return a
def menu():
    print('Choose Acton.\n Type "add" for new entree.\n Type "stat" to load statistic.\n Type "show" to see the entrees list.\n Type "exit" to quit')
    choose = input('...? ')
    if choose == 'add':
        Add_entrees()
    elif choose == 'show':
        print(db)
        menu()
    elif choose == 'stat':
        Statistics(stat)
def Add_entrees():
    n = int(input('please input count of entrees: '))
    a = Icalculate()
    end_of_while= a + n
    while a < end_of_while:
        new_db.setdefault(a)
        a += 1
    for key in new_db:
        new = entree.copy()
        for k in entree:             
            new[k]=input(f"input {k} ")             
        new_db[key]=new
        print('OK')
    db.update(new_db)
    new_db.clear()
    menu()
def Statistics(stat):
    for k,v  in db.items():
        for el in v:
            stat[el].append(v.get(el))
    print(stat)
    for k in stat:
        stat[k] = []
    menu()
menu()

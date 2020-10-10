print('-'*40)
print('Welcome to warehouse')
print('-'*40)
i = 1
choose = ''
entree = {"name":  "" , "price": "", "quantity": ""}
db = {i:entree}
stat = {"name": [], "price": [], "quantity": []} 
def menu():
    print('Choose Acton.\n Type "add" for new entree.\n Type "stat" to load statistic.\n Type "show" to see the entrees list.\n Type "exit" to quit')
    choose = input('...? ')
    if choose == 'add':
        Add_entrees(i)
    elif choose == 'show':
        print(db)
        menu()
    elif choose == 'stat':
        Statistics()
def Add_entrees(i):
    n = int(input('please input count of entrees: '))
    while i <= n:
        db.setdefault(i)
        i += 1
    for key in db:
        new = entree.copy()
        for k in entree:             
            new[k]=input(f"input {k} ")             
        db[key]=new
        print('OK')
    menu()
def Statistics():
    for k,v  in db.items():
        for el in v:
            stat[el].append(v.get(el))
    print(stat)
    menu()
menu()

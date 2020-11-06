'''
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
 и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве
  единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь
'''
from ex4 import Warehouse, Office_equipment, Printer, Scanner, Copier
from ex6 import MyOwnExeption

def main_menu():
  a = input('Welcome to warehouse. Choose Branch: \n 1) Office Equipment \n 2) at work \nOr type "exit" to quit... ')
  if a == '1':
    office_menu()
  elif a == 'exit':
    return None
  else:
    print('\nIncorrect input\n')
    main_menu()

def office_menu():
  a = input('Welcome to office equipment branch! \n 1) Show all entries in DB \n 2) Put anything to WH \n 3) Claim anything out WH \n 4) Show org structure \n \n 9) Back \n ....? ')
  if a == '1':
    print(Office_equipment.show_all())
    return_menu()
  elif a == '2':
    add_menu()
  elif a == '3':
    claim_menu()
  elif a == '4':
    print(Warehouse.show_org_equipment())
    return_menu()
  elif a == '9':
    main_menu()
  else:
    print('\nIncorrect input\n')
    office_menu()

def return_menu():
  input('\n Action success, Push Enter to continue \n')
  office_menu()

def claim_menu():
  a = input('OK \nChoose what you want to claim from WH: \n 1) Printer \n 2) Scanner \n 3) Copier \n\n 9) Back \n ....?')  
  if a == '3':
    Copier.removeFromWH(choosing_dept(), int(input('How much copiers you need? ')))
    return_menu()
  elif a == '1':
    if Printer.removeFromWH(choosing_dept(), int(input('How much printers you need? '))) == False:
      fail_menu()
    else:     
      return_menu()
  elif a =='2':
    Scanner.removeFromWH(choosing_dept() ,int(input('How much scanners you need? ')))
    return_menu()
  else:
    print('\nIncorrect input\n')
    claim_menu()

def choosing_dept():
  a = input('\n Choose Departement, where you want use tech: \n 1) Callcentre \n 2) IT \n 3) Manager \n ...?')
  if a == '1':
    key = 'Callcenter'
  elif a == '2':
    key = 'IT'
  elif a =='3':
    key = 'Manager'
  return key

def fail_menu():
  input('\n Action Failed. Press Enter to back to menu. \n ')
  office_menu()


def add_menu():
  a = input('OK, lets go.\n Choose what you want to add: \n 1) Printer \n 2) Scanner \n 3) Copier \n\n 9) Back \n ....?')
  if a == '1':
    validation_func(a)
  elif a == '2':
    validation_func(a)
  elif a == '3':
    validation_func(a)
  else:
    print('\nIncorrect input\n')
    add_menu()


def validation_func(choose):
    if choose == '1':
        name = 'printers'
    elif choose == '2':
        name = 'scanners'
    elif choose == '3':
        name = "copiers"
    try:
        n = input(f'How much {name} you want to add? ')
        if MyOwnExeption.valid_number(n) == False:
          raise MyOwnExeption('You must eter numbers only!')
        else:
            if name == 'printers':
                Printer.income(int(n))
                return_menu()
            elif name == 'scanners':
                Scanner.income(int(n))
                return_menu()
            elif name == 'copiers':
                Copier.income(int(n))
                return_menu()

    except MyOwnExeption as err:
      print(err)
      fail_menu()
    

main_menu()
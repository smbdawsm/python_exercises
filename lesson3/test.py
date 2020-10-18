cont = True
def summ(array, new_list, n=0):
    for el in test_list:
        try:
            if el.upper() != "Q":
                new_list += [int(el)]
            elif el.upper() == "Q":
                n = test_list.index(el)
                break
        except (ValueError, IndexError):
            print("Вы ввели неверные значения! Постарайтесь соблюдать условия.")
    if test_list[n].upper == 'Q':
        cont = False
        return cont
    else:
        return sum(new_list)


new_list = []

while cont:
    test_list = input("Числа >>> ").split()
    print(f"Сумма последних введеных элементов: {summ(test_list, new_list)}")
    if cont==False:
        break
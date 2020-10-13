my_list = [7, 5, 3, 3, 2]
length = len(my_list)
a = int(input("Please input a your ratio 1-10:"))
for el in my_list:
    if a > el:
        if a < my_list[length-1]:
            i = my_list.index(el)
            my_list.insert(i, a)
            break
        else: continue
    else:
        my_list.append(a)
        break
print(my_list)

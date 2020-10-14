string = input("Please input a string here: ")
some_list = string.split()
i = 1
for el in some_list:
    print(f"Index: {i}, string: {el[:10]}")
    i += 1

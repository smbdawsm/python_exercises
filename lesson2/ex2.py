i = 1
length = int(input('Please input length of list: '))
some_list = []
while i <= length:
    a = input(f'Input {i} element please: ')
    some_list.append(a)
    i += 1
l = 0
print(some_list)
while l <= length:
    a = some_list.pop(l)
    some_list.insert(l+1, a)
    l += 2
print(some_list)

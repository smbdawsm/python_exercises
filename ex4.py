a = int(input('Please input A'))
max = 0
while a  > 0:
    mod_a = a % 10
    if mod_a > max:
        max = mod_a
    a = a // 10
print(f'Maximum is {max}')

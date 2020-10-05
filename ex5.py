dohod = int(input ('Viruchka = '))
rashod = int(input ('Izderjka = '))
if dohod == rashod:
    print('Firma nichego ne zarabotala')
elif dohod >= rashod:
    print(f'Firma zarabotala {dohod-rashod}, rentabelnost {(dohod-rashod)/dohod}')
    num = int(input('A skolko sotrudnikov v firme? '))
    print(f'Kajdiy sotrudnik zarabotal {(dohod-rashod)/num}')
else:
    print(f'Firma poteryala {rashod-dohod}')

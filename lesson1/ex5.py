dohod = int(input ('Viruchka = '))
rashod = int(input ('Izderjka = '))
if dohod == rashod:
    print('Firma nichego ne zarabotala')
elif dohod >= rashod:
    print(f'Firma zarabotala {dohod-rashod:.02f}, rentabelnost {(dohod-rashod)/dohod:.02f}')
    num = int(input('A skolko sotrudnikov v firme? '))
    print(f'Kajdiy sotrudnik zarabotal {(dohod-rashod)/num:.02f}')
else:
    print(f'Firma poteryala {rashod-dohod}')

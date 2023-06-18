nota = float(input('digite nota:'))
while nota < 0 or nota > 10: 
    print(f'{nota} invalida')
    nota = float(input('digite outra nota:'))

    print(f'ok{nota} valida')
usuario = input('digite um usuario:')
senha = input('digite seha:')

while usuario == senha:
    print('erro: usuario e senha sao identicos')
usuario = input('digite um usuario:')
senha = input('digite senha diferente de uuario:')
print('ok, usuario e senha validos')
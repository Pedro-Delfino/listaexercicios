while True:
    Ano = int(input('Digite o ano do carro que deseja comprar:'))
    valor = float(input('Informe o valor original do carro:'))
    if Ano <=2000:
        desconto = valor*(0.12)
        novovalor = valor - desconto
        print(f'O carro de R${valor}, com o desconto de 12% (R${desconto}), saira por R${novovalor}')
    else:
        desconto= valor*(0.07)
        novovalor = valor - desconto
        print(f'O carro de R${valor}, com o desconto de 12% (R${desconto}), saira por R${novovalor}')

    retorno = input('Deseja fazer outra consulta? S/N?')
    if retorno.upper() != "S":
        break

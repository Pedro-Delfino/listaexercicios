contador = 0
for i in range(80):
    Numero = int(input('Digite um número:'))
    if Numero > 9 and Numero < 151:
        contador +=1
print(f'{contador} numeros estão no intervalo entre 10 e 150')
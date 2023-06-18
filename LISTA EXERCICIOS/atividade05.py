n = int(input("digite a quantidade de notas:"))
soma = 0
for i in range(n):
    nota = float(input(f'digite a nota{i+1}:'))
    soma= soma + nota
print(soma)
media = soma//n
print(f'sua media foi:{nota}:')
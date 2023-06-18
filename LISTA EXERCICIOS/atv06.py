while True:
    Nome = input('digite seu nome:')
    Ra = input('digite seu número de identificação:')
    N1 = float(input('digite a nota 1:'))
    N2 = float(input('digite a nota 2:'))
    N3 = float(input('digite a nota 3:'))
    ME = float(input('digite a nota ME:'))
    print('-'*70)

    MA = (N1 + (N2*2) + (N3*3) + ME)/7


    if MA >= 9.0:
        conceito = 'A'
        
    elif 7.5 <= MA < 9.0:
        conceito = 'B'
        
    elif 6.0 <= MA < 7.5:
        conceito = 'C'
        
    elif 4.0 <= MA < 6.0:
        conceito = 'D'
        
    elif MA < 4.0:
        conceito = 'E'
    
    if conceito in ['A','B','C']:
        Aprovação ='Aprovado'
    elif conceito in ['D','E']:
        Aprovação = 'Reprovado'    

    print(f"Nome do Aluno:{Nome}")
    print(f"RA do aluno: {Ra} ")
    print(f"Notas: Nota1:{N1}, Nota2:{N2}, Nota3:{N3} ")
    print(f"Média dos exercícios: {ME} ")
    print(f"Média de aproveitamento: {MA} ")
    print(f"Conceito: {conceito} ")
    print(f"Aprovação: {Aprovação} ")

    Retorno = input("Deseja digitar as notas de outro aluno? (S/N): ")
    if Retorno.upper() != "S":
        break
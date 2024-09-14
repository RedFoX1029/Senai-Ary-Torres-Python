nome = input('Digite o nome: ')
materia = input('Digite o nome da matéria: ')

nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
nota3 = float(input('Digite a nota do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'\nNome: {nome}\nMatéria: {materia}\nMédia: {media:.1f}')

if (media >= 0) and media < 5:
    print('\033[1;31;42mReprovado\033[m')
elif (media >= 5) and media < 8:
    print('\033[1;34mEm recuperação')
elif (media >= 8) and (media <= 10):
    print('\033[1;32mAprovado!')
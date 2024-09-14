nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if (((nota1 + nota2) / 2) >= 0) and (((nota1 + nota2) / 2) < 5):
    print('Reprovado')
elif (((nota1 + nota2) / 2) >= 5) and (((nota1 + nota2) / 2) < 8):
    print('Em recuperação')
elif (((nota1 + nota2) / 2) >= 8) and (((nota1 + nota2) / 2) <= 10):
    print('Aprovado!')
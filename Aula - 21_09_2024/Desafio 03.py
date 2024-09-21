extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco')

while True:
    num = int(input('Digite um número Inteiro de 0 a 5: '))
    if 0<=num<=5:
        break
    print('Tente um número válido entre 0 a 5.')
print(f'Você digitou o número {extenso[num]}')
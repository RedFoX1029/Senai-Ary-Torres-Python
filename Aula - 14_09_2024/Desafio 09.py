peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / (altura ** 2)

if imc > 0 and imc < 18.5:
    print(f'O imc é:  {imc}, diagnóstico: Abaixo do peso.')
elif imc >= 18.5 and imc < 24.9:
    print(f'O imc é:  {imc}, diagnóstico: Peso normal.')
elif imc >= 24.9 and imc < 29.9:
    print(f'O imc é:  {imc}, diagnóstico: Excesso de peso.')
elif imc >= 29.9 and imc < 35:
    print(f'O imc é:  {imc}, diagnóstico: Obesidade.')
elif imc > 35:
    print(f'O imc é:  {imc}, diagnóstico: Obesidade extrema.')
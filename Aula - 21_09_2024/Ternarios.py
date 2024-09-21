while True:
    num = int(input('Digite um número: '))
    # Operadores ternários em uma atribuição de variável
    boolean = True if (num == 1) else False
    boolean2 = (False, True)[num == 1]

    # Operadores ternários em um print
    print('True' if boolean else 'False')  # Mesma coisa de 'if boolean == True'
    print(('Par', 'Impar')[boolean])  # Mesma coisa de 'if boolean == True'
    print(boolean2)

    print(f'\nDigite 0 pra sair.')

    if num == 0:
        break

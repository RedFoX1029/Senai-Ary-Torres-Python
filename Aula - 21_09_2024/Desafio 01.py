media = 0
frequencia = 0
while True:
    nota = int(input('Digite a nota (1 à 10): '))
    media += nota
    frequencia += 1
    escolha = input('Deseja continuar?\n[S] Sim\n[N] Não\n')
    if escolha.upper() == 'N': break

mediaFinal = media / frequencia

print(f'Sua nota: {mediaFinal:.1f}, e você foi:\n')

if (mediaFinal >= 0) and mediaFinal < 5:
    print('\033[1;31mReprovado\033[m')
elif (mediaFinal >= 5) and mediaFinal < 8:
    print('\033[1;34mEm recuperação')
elif (mediaFinal >= 8) and (mediaFinal <= 10):
    print('\033[1;32mAprovado!')
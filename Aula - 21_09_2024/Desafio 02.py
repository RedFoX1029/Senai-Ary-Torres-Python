import random
tentativas = 0
random = random.randint(1, 10)
while True:
    num = int(input('Adivinhe um número: '))
    tentativas += 1

    if num == random:
        print(f'\nPARABÉNS!!!!\nNúmero de tentativas: {tentativas}\nNúmero sorteado: {random}')
        break

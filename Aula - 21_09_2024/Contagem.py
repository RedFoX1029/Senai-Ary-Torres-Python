itens = []
qtd = 0
for i in range(1, 4):
    num = int(input('Digite um número: '))
    itens.append(num)
for i in itens:
    if i % 2 == 0:
        qtd += 1
print(qtd)
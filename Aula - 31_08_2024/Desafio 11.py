valor = float(input('Digite o valor do produto: '))
print(f'Valor original: R${valor:.2f}\nDesconto: R${(valor * 0.05):.2f}\nValor com o desconto: {valor - (valor * 0.05):.2f}')
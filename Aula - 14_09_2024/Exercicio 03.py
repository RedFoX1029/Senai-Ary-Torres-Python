datas = []
for i in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    if ano <= 2006:
        datas.append(ano)
for i in datas:
    print(i)
time1 = int(input('Digite os gols do primeiro time: '))
time2 = int(input('Digite os gols do segundo time: '))

if time1 == time2:
    print('Empate')
elif time1 > time2:
    print(f'O primeiro time ganhou de {time1} x {time2} ')
else:
    print(f'O segundo time ganhou de {time2} x {time1} ')
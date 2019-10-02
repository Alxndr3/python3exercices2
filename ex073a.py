print(20 * '/-')
print('         Tabela do Brasileirão')
print(20 * '/-')
classificação = ('Flamengo', 'Santos', 'São Paulo', 'Palmeiras', 'Corinthians', 'Atletico-MG',
                 'Internacional', 'Bahia', 'Botafogo', 'Athletico', 'Grêmio', 'Goiás', 'Ceará',
                 'Vasco', 'Fortaleza', 'Cruzeiro', 'Chapecoense', 'Fluminense', 'CSA', 'Avaí')
ver = None
while type(ver) is not int:
    try:
        ver = int(input('''Digite: 
1 para ver os 5 primeiros colocados. 
2 para ver os 4 ultimos.
3 para ver os times em ordem alfabética.
4 para ver a lista toda.
5 para ver a posição do time desejado: '''))
    except ValueError:
        print(end='Tente novamente. ')
if ver == 1:
    print(classificação[0:5])
elif ver == 2:
    print(classificação[-4:])
elif ver == 3:
    print(sorted(classificação))
elif ver == 4:
    for c, f in enumerate(classificação):
        print(1 + c, f)
elif ver == 5:
    time = str(input('Qual time deseja ver? ')).strip().title()
    while time not in classificação:
        time = str(input('Este time não esta na tabela, tente novamente: ')).strip().title()
    count = 0
    for meutime in classificação:
        count += 1
        if time == meutime:
            print(f'O {meutime} está em {count}° lugar.')
#print(f'O Athletico esta em {classificação.index("Athletico")}°')






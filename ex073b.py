times = ('Flamengo', 'Santos', 'São Paulo', 'Palmeiras', 'Corinthians', 'Atletico-MG',
                 'Internacional', 'Bahia', 'Botafogo', 'Athletico', 'Grêmio', 'Goiás', 'Ceará',
                 'Vasco', 'Fortaleza', 'Cruzeiro', 'Chapecoense', 'Fluminense', 'CSA', 'Avaí')
print(15 * '-=')
print(f'Lista de Times: {times}')
print(15 * '-=')
print(f'Os 5 primeiros são: {times[0:5]}')
print(15 * '-=')
print(f'Os 4 ultimos são: {times[-4:]}')
print(15 * '-=')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(15 * '-=')
print(f'O Athletico esta na {times.index("Athletico") + 1} posição')
print(15 * '-=')

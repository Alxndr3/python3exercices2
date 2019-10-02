tg = mm = mp = c = 0
while True:
    np = str(input('Digite o nome do produto: ')).strip().title()
    pp = float(input('Digite o preço do produto: R$'))
    c += 1
    tg += pp
    if c == 1 or pp < mp:
        mp = pp
        npb = np
    if pp > 1000:
        mm += 1
    dc = ' '
    while dc not in 'sn':
        dc = str(input("Deseja continuar: [S/N] ")).strip().lower()[0]
    if dc == 'n':
        break
if mm == 1:
        print(f'{mm} produto custa mais de mil Reais.')
else:
    print(f'{mm} produtos custam mais de mil Reais')
print(f'O produto {npb} foi o mais barato custando R${mp:.2f}')
print(f'O total gasto na compra foi R${tg:.2f}')


l = []
while True:
    l.append(int(input('Digite um número: ')))
    c = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if c == 'N':
        break
print(f'A lista possui {len(l)} elementos.')
l.sort(reverse=True)
print(f'Os valores em ordem decrescente são {l}')
if 5 in l:
    print(f'Número 5 na lista.')
else:
    print('Número 5 não inserido.')


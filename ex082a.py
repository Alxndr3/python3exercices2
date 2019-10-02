l = []
p = []
imp = []
while type(int):
    try:
        i = int(input('Digite um número: '))
        l.append(i)
    except ValueError:
        print('Opção inválida: ')
        continue
    else:
        x = str(input('Desaja inserir um novo número? [S/N]: ')).strip().upper()
    while x not in 'SN':
        x = str(input('Desaja inserir um novo número? [S/N]: ')).strip().upper()
    if x == 'N':
        break
for x in l:
    if x % 2 == 0:
        p.append(x)
    else:
        imp.append(x)
print(f'Os números inseridos foram: {l}')
print(f'Os números pares inseridos foram: {p}')
print(f'Os números ímpares inseridos foram: {imp}')


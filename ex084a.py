l = []
d = []
npe = []
nle = []
c = pe = le = 0
while True:
    d.append(str(input('Nome: ')).strip().title())
    d.append(int(input('Peso: ')))
    l.append(d[:])
    d.clear()
    if c == 0:
        pe = le = l[0][1]
    k = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    c += 1
    if k == 'N':
        break
for x in l:
    if x[1] > pe:
        pe = x[1]
    if x[1] < le:
        le = x[1]
for y in l:
    print(y)
    if y[1] == pe:
        npe.append(y[0])
        print(npe)
    if y[1] == le:
        nle.append(y[0])
print(f'{c} pessoas cadastradas')
print(f'O maior peso é {pe} de {npe}')
print(f'O menor peso é {le} de {nle}')



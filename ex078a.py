lista = list()
ima = list()
ime = list()
c1 = c2 = ma = me = 0
for r in range(1, 6):
    l = int(input('Digite um valor: '))
    lista.append(l)
    if r == 1:
        ma = l
        me = l
    else:
        for x in lista:
            if x > ma:
                ma = x
                c1 += 1
            if x < me:
                me = x
                c2 += 1
for e, x in enumerate(lista):
    if x == ma:
        ima.append(e)
        c1 += 1
    if x == me:
        ime.append(e)
        c2 += 1
print(f'Os números digitados foram {lista}')
if c1 == 1:
    print(f'O maior valor digitado foi {ma} na posição: ', end=' ')
    for z in ima:
        print(z, end=' ')
else:
    print(f'O maior valor digitado foi {ma} nas posições', end=' ')
    for z in ima:
        print(z, end=' ')
if c2 == 1:
    print(f'\nO menor valor digitado foi {me} na posição', end=' ')
    for z in ime:
        print(z, end=' ')
else:
    print(f'\nO menor valor digitado foi {me} nas posições', end=' ')
    for z in ime:
        print(z, end=' ')



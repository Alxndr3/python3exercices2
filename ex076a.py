print(35 * '-')
print(f'{"LISTA DE PREÇOS":^36}')
print(35 * '-')
count = 0
lista = []
tupla = []
for c in range(0, 3):
    if count == 0:
        lista = str(input('Digite um produto: ')).strip().title(), float(input('Digite o seu preço: R$ '))
        tupla.append(lista)
        count += 1
    else:
        lista = str(input('Digite outro produto: ')).strip().title(), float(input('Digite o seu preço: R$ '))
        tupla.append(lista)
for i in tupla:
    print(f'{i[0]:-<20}R${i[1]: <4}')

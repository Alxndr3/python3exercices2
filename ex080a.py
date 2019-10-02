i = int(input('oi Digite um valor: '))
l = [i]
print('Valor adicionado ao final da lista.')
i = int(input('Insira um número: '))
if i < l[0]:
    l.insert(0, i)
    print('Inserido na posição 0')
else:
    l.append(i)
    print('Inserido na posição 1')
for x in range(1, 4):
    i = int(input('Insira um número: '))
    if i <= l[0]:
        l.insert(0, i)
        print('Inserido na posição 0')
        continue
    elif l[0] <= i < l[1]:
        l.insert(1, i)
        print('Inserido na posição 1')
        continue
    elif l[1] <= i:
        l.append(i)
        print('Iserido na posição 2')
        continue
    elif l[2] <= i:
        l.append(i)
        print('Iserido na posição 3')
        continue
print('Os valores digitador em orem foram', l)

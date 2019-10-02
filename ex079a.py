v = []
while type(int):
    try:
        i = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Opção inválida. ')
        continue
    if i not in v:
        v.append(i)
    else:
        c = str(input('Valor já inserido, deseja continuar? [S/N]: ')).strip().upper()
        while c not in 'SN':
            c = str(input('Opção inválida tente novamente [S/N]: '))
        if c == 'N':
            break
    s = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while s not in 'SN':
        s = str(input('Opção inválida tente novamente [S/N]: ')).strip().upper()
    if s == 'N':
        print('Obrigado, e até logo.')
        break
v.sort()
print(25 * '-=')
print(f'Os valores digitados foram {v}')

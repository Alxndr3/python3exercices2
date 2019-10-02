n = maior = menor = int(input('Digite um número: '))
c = 'S'
m = 0
cont = 1
while c == 'S':
    c = str(input('Deseja digitar outro? [S/N]: ')).upper()
    if c == "S":
        i = int(input('Novo número: '))
        n += i
        cont += 1
        m = n / cont
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    else:
        print('FIM')
print(f'A soma entre os números digitados é {n}, a média é {m :.2f}, o maior é {maior} e o menor é {menor}')



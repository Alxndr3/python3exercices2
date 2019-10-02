n3 = 0
tupla = []
np = []
n3l = []
for i in range(0, 4):
    num = int(input('Digite um número: '))
    tupla.append(num)
    if num == 3:
        n3 = i + 1
        n3l.append(n3)
    if num % 2 == 0:
        np.append(num)
print('Você digitou os números', tuple(tupla))
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if n3 <= 0:
    print('O número 3 não foi digitado')
else:
    print(f'O númro 3 apareceu na posição {n3l}')
if np == []:
    print('Não foram digitados números pares.')
else:
    print(f'Os números pares digitados foram {tuple(np)}')


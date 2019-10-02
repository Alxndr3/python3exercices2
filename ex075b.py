n3 = n9 = 0
np = []
tupla = []
for i in range(0, 4):
    num = int(input('Digite um número: '))
    tupla.append(num)
    if num % 2 == 0:
        np.append(num)
    if num == 9:
        n9 += 1
    if num == 3:
        n3 = i + 1

print('Você digitou os números', tuple(tupla))
print(f'O valor 9 apareceu {n9} vezes')
if n3 <= 0:
    print('O número 3 não foi digitado')
else:
    print(f'O número 3 apareceu na posição {n3}')
print(f'Os números pares digitados foram {np}')

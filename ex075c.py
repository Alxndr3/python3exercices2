num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o ultimo número: ')))
print(f'Vocẽ digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1} posição')
else:
    print('O Número 3 não foi digitado.')
for n in num:
    if n % 2 == 0:
        print(n, end=" ")

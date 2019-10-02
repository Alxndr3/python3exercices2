from random import sample
shuf = tuple(sample((range(11)), k=5))
print(shuf)
maior = menor = cont = 0
for me in shuf:
    cont += 1
    if cont == 1:
        maior = menor = me
    if me > maior:
        maior = me
    if me < menor:
        menor = me
print(f'O maior valor sorteado foi {maior} e o menor foi {menor}')
print(f'O maior foi {max(shuf)} o menor foi {min(shuf)}')
print(type(shuf))


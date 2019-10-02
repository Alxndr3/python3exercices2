c = d = 0
s = int(input('Digite um número: '))
while s != 999:
    c += 1
    d += s
    s = int(input('Digite um número: '))
print(f'Você digitou {c} números, a soma entre eles é {d}')

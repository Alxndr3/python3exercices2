l = list()
c1 = c2 = 0
expressão = str(input('Digite uma expressão matemática: ')).strip()
for x in expressão:
    if '(' in x:
        c1 += 1
    if ')' in x:
        c2 += 1
if (c1 + c2) % 2 == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')

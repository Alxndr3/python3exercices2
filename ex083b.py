expressao = list(str(input('Digite uma expressão matemática: ')).strip())
ap = expressao.count('(')
fp = expressao.count(')')
if (ap + fp) % 2 == 0:
    print('Expressão correta')
else:
    print('Expressão errada')


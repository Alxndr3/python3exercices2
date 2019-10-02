tupla = ('aprender', 'programar', 'linguagem', 'pythom', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for x in palavra:
        if x in 'aeiou':
            print(x, end=' ')




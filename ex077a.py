palavras = ('aprender', 'programar', 'linguagem', 'pythom', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for x in palavras:
    a = 'a' in x
    e = 'e' in x
    i = 'i' in x
    o = 'o' in x
    u = 'u' in x
    vogais = ' '
    if a == True:
        vogais = 'a'
    if e == True:
        vogais = vogais + 'e'
    if i == True:
        vogais = vogais + 'i'
    if o == True:
        vogais = vogais + 'o'
    if u == True:
        vogais = vogais + 'u'
    print(f'Na palavra {x.upper()}, temos {vogais}')


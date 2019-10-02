ci = ch = cm = 0
print('-' * 35)
print('Cadastre um Pessoa')
print('-' * 35)
while True:
    ida = int(input('Idade: '))
    sex = str(input('Sexo: [M/F] ')).strip().lower()
    while sex not in 'mf':
        sex = str(input('Sexo: [M/F] ')).strip().lower()
    if ida > 18 and sex == 'm':
        ci += 1
    if sex == 'm':
        ch += 1
    elif sex == 'f' and ida < 20:
        cm += 1
    k = str(input('Deseja continuar: [S/N] ')).strip().lower()
    while k != 's' and k != 'n':
        k = str(input('Deseja continuar: [S/N] ')).strip().lower()
    else:
        break
print(f'{ci} homens com mais de 18 anos, total de homens {ch}, Mulheres com menos de 20 {cm}')



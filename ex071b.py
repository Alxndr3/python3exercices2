print('=' * 21)
print(':^30'.format('===BANCO ALEXANDRE==='))
print('=' * 21)
valor = int(input("Quanto quer sacar? R$"))
saq = valor
ced = 50
totced = 0
while True:
    if saq >= ced:
        saq-= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} Cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if saq == 0:
            break


numero = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while escolha not in range(0, 21):
    escolha = int(input('Tente Novamente: Digite um número de 0 a 20: '))
for num in numero:
    print(f'Você digitou o número {numero[escolha]}')
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Você deseja continuar? S/N: ')).strip().upper()
    if conti == 'N':
        print('Até logo.')
        break
    else:
        escolha = int(input('Digite um número de 0 a 20: '))
        while escolha not in range(0, 21):
            escolha = int(input('Digite um número de 0 a 20: '))


cont = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
while True:
    num = None
    while type(num) is not int:
        try:
            num = int(input('Digite um número de 0 a 20: '))
        except ValueError:
            print(end='Opção inválida. ')
    if 0 <= num <= 20:
        print(f'Vocẽ digitou o número {cont[num]}')
        mais = ' '
        while mais not in 'SN':
            mais = str(input('Deseja continuar? S/N: '))[0].strip().upper()
        if mais == 'N':
            print('Adeus')
            break
    else:
        print('Tente novamente!! ', end='')


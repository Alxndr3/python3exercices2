from random import randint
print('-=' * 20, '\n VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
c = randint(1, 10)
co = 0
while True:
    poi = str(input('Par ou Impar? ')).strip().lower()[0]
    j = int(input('Diga seu valor: '))
    if poi == 'p' and (c + j) % 2 == 0:
        par = c + j
        print('Você Ganhou!')
        print(f'Computador jogou {c} e você jogou {j}, {par} é par.')
        co += 1
    elif poi == 'i' and (c + j) % 2 == 1:
        impar = c + j
        print(('Você Ganhou!'))
        print(f'Computador jogou {c} e você jogou {j}, {impar} é ímpar.')
        co += 1
    else:
        if poi == 'p':
            impar = c + j
            print(f'Computador jogou {c} e você jogou {j}, {impar} é ímpar.')
            print('Game Over!')
            if co == 0:
                print('Você ganhou nem uma vez.')
            else:
                print(f'Você ganhou {co} vezes.')
            break
        else:
            par = c + j
            print(f'Computador jogou {c} e você jogou {j}, {par} é par.')
            print('Game Over!')
            if co == 0:
                print('Você ganhou nem uma vez.')
            else:
                print(f'Você ganhou {co} vezes.')
            break



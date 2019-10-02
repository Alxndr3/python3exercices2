while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if t <= 0:
        break
    else:
        x = 0
        for x in range(1, 11):
            y = t * x
            print(f'{t} x {x} = {y}')
        print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO, Volte sempre.')

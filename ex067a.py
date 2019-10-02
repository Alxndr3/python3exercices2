while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t <= 0:
        print('Stoping...')
        break
    else:
        x = 0
        for x in range(1, 11):
            y = t * x
            print(f'{t}x{x}={y}')



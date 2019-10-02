t = int(input('\033[33mDigite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
q = int(input('Quantos termos? '))
c = 0
while c < q:
    t += r
    c += 1
    print('Termo {} = {}'.format(c, t))
m = str(input('Deseja continuar vendo os termos? \033[1;35m[S/N]\033[m: ')).upper()
while m == 'S':
    q = c + int(input('\033[36mQuantos termos? '))
    while c < q:
        t += r
        c += 1
        print('Termo {} = {}'.format(c, t))
    m = str(input('Deseja continuar vendo os termos? \033[1;35m[S/N]\033[m: ')).upper()

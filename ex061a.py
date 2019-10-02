t = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
while c < 10:
    t += r
    c += 1
    print('Termo {} = {}'.format(c, t))

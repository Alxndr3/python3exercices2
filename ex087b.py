l = [[], [], []]
c = s = d = 0
for x in range(0, 3):
    for y in range(0, 3):
        d = int(input(f'Digite um valor para [{x}, {y}]: '))
        l[x].append(d)
        if d % 2 == 0:
            s += d
        c += l[x][2]
for z in range(0, 3):
    print(f'[ {l[z][0]} ] [ {l[z][1]} ] [ {l[z][2]} ]')
print(f'A soma dos valores pares é {s}')
print(c)

l = [[], [], []]
s = c = g = 0
for x in range(0, 3):
    for y in range(0, 3):
        l[x].append(int(input(f'Digite um valor para [{x}, {y}]: ')))
for z in range(0, 3):
    print(f'[ {l[z][0]} ] [ {l[z][1]} ] [ {l[z][2]} ]')
for e in range(0, 3):
    for d in range(0, 3):
        if l[e][d] % 2 == 0:
            s += l[e][d]
    c += l[e][2]
    if l[1][e] > g:
        g = l[1][e]
print(f'The sum of the even values is: {s}')
print(f'The sum of third column is: {c}')
print(f'The greatest num form second row is: {g}')

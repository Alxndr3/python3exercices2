l = [[], [], []]
s = 0
for x in range(0, 3):
    for y in range(0, 3):
        l[x].append(int(input(f'Digite um valor para [{x}, {y}]: ')))
for z in range(0, 3):
    print(f'[ {l[z][0]} ] [ {l[z][1]} ] [ {l[z][2]} ]')

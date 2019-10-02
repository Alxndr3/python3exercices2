l = [[], []]
for x in range(1, 8):
    n = int(input(f"Digite o {x}o. número: "))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
print(f'Pares: {sorted(l[0])}')
print(f'Ímpares: {sorted(l[1])}')



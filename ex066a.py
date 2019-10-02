c = t = 0
while True:
    i = float(input('Digite um valor [999 para parar]: '))
    if i == 999:
        break
    t += i
    c += 1
print(f'A soma dos {c} valores é {t}')




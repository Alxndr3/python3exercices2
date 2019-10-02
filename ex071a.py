print('=' * 21)
print('===BANCO ALEXANDRE===')
print('=' * 21)
saq = int(input("Quanto quer sacar? "))
while True:
    if saq > 50:
        ci = saq // 50
        saq %= 50
        print(f'{ci} notas de 50')
    else:
        if saq >= 20:
            vi = saq // 20
            saq %= 20
            print(f'{vi} notas de 20')
        else:
            if saq >= 10:
                de = saq // 10
                saq %= 10
                print(f'{de} notas de 10')
            else:
                if saq >= 5:
                    cin = saq // 5
                    saq %= 5
                    print(f'{cin} notas de 5')
                if saq == 0:
                    break
                else:
                    if saq > 0:
                        um = saq // 1
                        saq %= 1
                        print(f'{um} notas de 1')

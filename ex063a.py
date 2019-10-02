from time import sleep
e = int(input('Quantos elementos deseja ver? '))
f1 = 0
f2 = 1
n = 0
print(f1, end=' - ')
print(f2, end=' - ')
while n in range(e):
  f3 = f1 + f2
  f1 = f2
  f2 = f3
  n += 1
  sleep(0.5)
  print(f3, end=' - ')
print('FIM')





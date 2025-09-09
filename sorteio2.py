import random
print('---------------------------')
print('         SORTEIO 2         ')
print('---------------------------')
numero_sorteado = random.randint(0,10)
c = 0
while True:
    c += 1
    p = int(input('Qual número pensei: '))
    if p == numero_sorteado:
        print(f'O número sorteado foi {numero_sorteado} e você teve {c} tentativas.')
        break

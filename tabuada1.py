print('---------------------------------')
print('             TABUADA             ')
print('---------------------------------')

inicio = int(input('Onde inicia: '))
fim = int(input('Onde termina: '))              #declaração de variáveis
op = input('Qual operador (+,-,*,/): ')
n1 = int(input('Digite um número: '))

if inicio < fim:
    if op == '*':
        for i in range(inicio,fim+1):
            print(f'{n1} * {i} = {n1*i}')
        print('FIM')
    elif op == '+':
        for i in range(inicio,fim+1):
            print(f'{n1} + {i} = {n1+i}')       #script de calculo
        print('FIM')
    elif op == '-':
        for i in range(inicio,fim+1):
            print(f'{n1} - {i} = {n1-i}')
        print('FIM')
    elif op == '/':
        for i in range(inicio,fim+1):
            print(f'{n1} / {i} = {n1/i}')
        print('FIM')
else:
    print('ERRO')
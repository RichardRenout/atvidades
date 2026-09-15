import os
os.system('cls')

valor_a = int(input('Digite um número: '))
valor_b = int(input('Digite um número: '))
valor_c = int(input('Digite um número: '))

soma = (valor_a + valor_b)

if soma > valor_c:
    print('A + B é maior que C')
else: print('A + B é menor que C')
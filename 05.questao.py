import os
os.system('cls')

# Faça um programa que leia um código de operação (+, -, *, ou /) e também dois valores inteiros A e B.
# O programa deve calcular o resultado da operação escolhida aplicada a A e B.
# Por exemplo, se a operação escolhida foi * e A = 1 e B = 3,
# o programa deve fornecer como resultado o valor de 1 * 3, que é 3.

numero1 = float(input('Digite um número: '))
operacao = input('Digite uma operacao: ')
numero2 = float(input('Digite um número: '))

match operacao:
    case '+':
        soma = numero1 + numero2
        print(f'o valor {numero1} {operacao} {numero2}, é {soma}')
    case '-':
        subtracao = numero1 - numero2
        print(f'o valor {numero1} {operacao} {numero2}, é {subtracao}')
    case '*':
        multiplicacao = numero1 * numero2
        print(f'o valor {numero1} {operacao} {numero2}, é {multiplicacao}')
    case '/':
        divisao = numero1 / numero2
        print(f'o valor {numero1} {operacao} {numero2}, é {divisao}')
    case _:
        print('Inválido.')
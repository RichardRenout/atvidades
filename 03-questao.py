import os
os.system('cls')
# Faça um algoritmo que leia dois valores inteiros A e B.
# Se os valores forem iguais, deverá se somar os dois; caso contrário, multiplique A por B.
# Ao final de qualquer um dos cálculos, deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

valor_a = int(input('Digite um número: '))
valor_b = int(input('Digite um número: '))

if valor_a == valor_b:
    resultado = valor_a + valor_b
    c = resultado
    print(c)
else:
    resultado = (valor_a * valor_b)
    c = resultado
    print(c)
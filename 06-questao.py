import os
os.system('cls')

# Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas.
# O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 6,0);
# caso a média esteja entre 4,1 e 5,9, o aluno está em recuperação; caso a média seja inferior a 4,0, o aluno será reprovado.

nota_um = float(input('Sua primeira nota: '))
nota_dois = float(input('Sua segunda nota: '))
media_aritimetica = ((nota_um + nota_dois) / 2)

if media_aritimetica >= 6:
    print('Parabéns!')
elif media_aritimetica >= 4.1 and media_aritimetica <= 5.9:
    print('O aluno está em recuperação.')
else: print('O aluno está reprovado.')
import os
os.system('cls')

# Uma financeira usa o seguinte critério para conceder empréstimos:
# o valor total do empréstimo deve ser até dez vezes o valor da renda mensal do solicitante,
# e o valor da prestação deve ser no máximo 30% da renda mensal do solicitante.
# Escreva um programa que leia a renda mensal de um solicitante,
# o valor total do empréstimo solicitado e o número de prestações que
# o solicitante deseja pagar e informe se o empréstimo pode ou não ser concedido.

renda_mensal = float(input('Renda mensal: '))
valor_total_emprestimo = float(input('Valor do empréstimo: '))
if valor_total_emprestimo <= (renda_mensal * 10):
    numero_de_prestacoes = float(input('Quantas prestações deseja ? '))
    valor_prestacao = valor_total_emprestimo / numero_de_prestacoes
    if valor_prestacao <= (renda_mensal * 0.30):
        print('Empréstimo pode ser concedido.')
    else: print('Empréstimo não pode ser concedido.')
else: print('Empréstimo não pode ser concedido.')
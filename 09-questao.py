import os
os.system('cls')

renda_mensal = float(input('Digite sua renda mensal: '))

prestacoes = float(input('Digite o numero de prestações desejadas: '))

valor_total = (renda_mensal * prestacoes / 100)
print('valor: ',valor_total)

if prestacoes <= 30:
    print('Prestação Aceita!')
else:
    print('Prestação Não Aceita!')
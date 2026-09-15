import os
os.system('cls')

# Faça um algoritmo para ler: a descrição do produto (nome),
# a quantidade adquirida e o preço unitário.
# Calcular e
# escrever o total (total = quantidade adquirida * preço unitário),
# o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
# Se quantidade <= 5, o desconto será de 2%.
# Se quantidade > 5 e quantidade <= 10, o desconto será de 3%.
# Se quantidade > 10, o desconto será de 5%.

nome = input('Qual a descrição do produto: ')
quantidade_adquirida = int(input('Quantidade adquirida: '))
preco_unitario = int(input('Preço unitário: '))

total = quantidade_adquirida * preco_unitario

if quantidade_adquirida <= 5:
    valor_a_pagar = total * 0.02
    print(f'Valor: R${total}')
    print(f'Desconto: {0.02 * 100}')
    print(f'Valor com desconto: R${total - valor_a_pagar}')
elif quantidade_adquirida > 5:
    valor_a_pagar = total * 0.03
    print(f'Valor: R${total}')
    print(f'Desconto: {0.03 * 100:.0f}%')
    print(f'Valor com desconto: R${total - valor_a_pagar}')
elif quantidade_adquirida > 10:
    valor_a_pagar = total * 0.05
    print(f'Valor: R${total}')
    print(f'Desconto: {0.05 * 100:.0f}%')
    print(f'Valor com desconto: R${total - valor_a_pagar}')


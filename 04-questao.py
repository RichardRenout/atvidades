import os
os.system('cls')

# Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
# maçãs adquiridas e escreva o valor a ser pago pelo cliente.

print('--------------------------------------------')
print('|Frutas  |  Até 5 Kg      | Acima de 5 Kg  |')
print('|Morango | R$ 2,50 por Kg | R$ 2,20 por Kg |')
print('|Maçã    | R$ 1,80 por Kg | R$ 1,50 por Kg |')
print('--------------------------------------------')

morango = float(input('Quantos de morango Kg deseja ? '))
maca = float(input('Quantos de maça Kg deseja ? '))

if morango > 5:
    valor_morango = morango * 2.20
else: valor_morango = morango * 2.50

if maca > 5:
    valor_maca = maca * 1.50
else: valor_maca = maca * 1.80

valor_total = valor_morango + valor_maca
total_kg = morango + maca

if total_kg > 10 or valor_total > 15:
    valor_total * 0.10
    print(f'Você comprou: KG {total_kg}')
    print(f'A compra deu : R$ {valor_total:.2f}')






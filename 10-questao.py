import os
os.system('cls')

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A/G): ").upper()

match tipo:
    case "A":
        preco = 3.79

        if litros <= 25:
            desconto = 0.10
        else:
            desconto = 0.20

    case "G":
        preco = 6.59

        if litros <= 25:
            desconto = 0.15
        else:
            desconto = 0.30

    case _:
        print("Combustível inválido")
        exit()

valor = litros * preco
valor_desconto = valor * desconto
total = valor - valor_desconto

print(f"Valor a pagar: R$ {total:.2f}")
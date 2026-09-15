import os
os.system('cls')
# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
# Caso o sexo seja “F” e o estado civil seja “CASADA”, solicitar o tempo de casada (em anos).
# Por fim, mostre os dados do usuário.

nome = input('Digite seu nome: ')
sexo = input('Sexo: ').upper()
estado_civil = input('Estado Civil: ').upper()

if sexo == 'F' and estado_civil == 'CASADA':
    tempo_de_casada = int(input('Tempo de casada em anos: '))
    print(f'{nome}\n{sexo}\n{estado_civil}\n{tempo_de_casada}')
else: print(f'{nome}\n{sexo}\n{estado_civil}')


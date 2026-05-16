A = [0, 0, 0, 0, 0, 0]

indice = 0
while indice < 6:
    entrada = input(f'Digite o {indice + 1}º valor: ')
    if not entrada.isdigit():
        print('Inválido! Digite apenas números inteiros.')
        continue
    A[indice] = int(entrada)
    indice += 1

print('\nValores lidos:')
valores = 0
while valores < 6:
    print(f'A[{valores}] = {A[valores]}')
    valores += 1
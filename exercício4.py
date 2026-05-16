A = [0, 0, 0, 0, 0, 0, 0, 0]

posicao_leitura = 0
while posicao_leitura < 8:
    entrada = input(f'Digite o {posicao_leitura + 1}º valor: ')
    A[posicao_leitura] = int(entrada)
    posicao_leitura += 1

posicao_x = int(input('\nDigite a posição X (0 a 7): '))
posicao_y = int(input('Digite a posição Y (0 a 7): '))


soma = A[posicao_x] + A[posicao_y]

print(f'Valor na posição X ({posicao_x}): {A[posicao_x]}')
print(f'Valor na posição Y ({posicao_y}): {A[posicao_y]}')
print(f'Soma: {A[posicao_x]} + {A[posicao_y]} = {soma}')
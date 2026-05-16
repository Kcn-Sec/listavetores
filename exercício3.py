
A = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
B = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


posicao_leitura = 0
while posicao_leitura < 10:
    entrada = input(f'Digite o {posicao_leitura + 1}º valor: ')
    A[posicao_leitura] = float(entrada)
    posicao_leitura += 1


posicao_calculo = 0
while posicao_calculo < 10:
    B[posicao_calculo] = A[posicao_calculo] ** 2
    posicao_calculo += 1


print('\n====== VETOR A (originais) ======')
posicao_exibicao_a = 0
while posicao_exibicao_a < 10:
    print(f'A[{posicao_exibicao_a}] = {A[posicao_exibicao_a]}')
    posicao_exibicao_a += 1

print('\n====== VETOR B (quadrados) ======')
posicao_exibicao_b = 0
while posicao_exibicao_b < 10:
    print(f'B[{posicao_exibicao_b}] = {B[posicao_exibicao_b]}')
    posicao_exibicao_b += 1
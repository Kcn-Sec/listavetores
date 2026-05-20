vetor = [0.0] * 10
print('Digite 10 números reais:')

for i in range(10):
    vetor[i] = float(input(f'Posição {i + 1}: '))

negativos = 0
soma_positivos = 0.0

for i in range(10):
    if vetor[i] < 0:
        negativos += 1
    else:
        soma_positivos += vetor[i]

print(f'Vetor: {vetor}')
print(f'Quantidade de números negativos: {negativos}')
print(f'Soma dos números positivos: {soma_positivos:.2f}')
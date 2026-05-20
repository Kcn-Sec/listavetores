vetor = [0] * 10
print('Digite 10 números inteiros:')
for i in range(10):
    vetor[i] = int(input(f'Número {i + 1}: '))

maior = vetor[0]
posicao = 0

for i in range(10):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i

print(f'Vetor: {vetor}')
print(f'Maior elemento: {maior}')
print(f'Posição do maior elemento: {posicao + 1}')
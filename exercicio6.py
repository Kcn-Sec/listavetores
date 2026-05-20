vetor = [0] * 10
print('Digite 10 números inteiros:')
for i in range(10):
    vetor[i] = int(input(f'Posição {i + 1}: '))

maior = vetor[0]
menor = vetor[0]

for i in range(10):
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]

print(f'Vetor: {vetor}')
print(f'Maior elemento: {maior}')
print(f'Menor elemento: {menor}')


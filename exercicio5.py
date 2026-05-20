vetor = [0] * 10

print('Digite 10 números inteiros:')

for i in range(10):
    vetor[i] = int(input(f'Número {i + 1}: ')) 

pares = 0
for i in range(10):
    if vetor[i] % 2 == 0:
        pares += 1

print(f'Vetor: {vetor}')
print(f'Quantidade de números pares: {pares}')


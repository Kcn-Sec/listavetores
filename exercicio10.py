vetor = [0.0] * 5
print('Digite 5 valores:')

for i in range(5):
    vetor[i] = float(input(f'Valor {i + 1}: '))


maior = vetor[0]
menor = vetor[0]
soma = 0.0

for i in range(5):
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
    soma += vetor[i]

media = soma / 5

print(f'Valores: {vetor}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Média dos valores: {media:.2f}')
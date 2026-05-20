vetor = [0.0] * 5
print('Digite 5 valores:')

for i in range(5):
    vetor[i] = float(input(f'Número {i + 1}: '))

maior = vetor[0]
menor = vetor[0]
posicao_maior = 0   
posicao_menor = 0

for i in range(5):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao_maior = i
    if vetor[i] < menor:
        menor = vetor[i]
        posicao_menor = i

print(f'Vetor: {vetor}')
print(f'Maior valor: {maior} (Posição {posicao_maior + 1})')
print(f'Menor valor: {menor} (Posição {posicao_menor + 1})')
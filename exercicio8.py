notas = [0] * 15
print('Digite as notas de cada aluno:')

for i in range(15):
    notas[i] = float(input(f'Aluno {i + 1}: '))

soma = 0

for i in range(15):
    soma += notas[i]

media = soma / 15

print(f'Notas: {notas}')
print(f'Média da turma: {media:.2f}')
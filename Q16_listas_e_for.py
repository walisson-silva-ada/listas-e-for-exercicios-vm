Questão 16 da lista de for

nome = input('Qual o nome do Aluno?: ')
idade = int(input('Idade do aluno: '))
provas = int(input('Quantas Provas o aluno fez? (quantidade minima 3): '))
notas = []
for i in range(1,provas+1):
        notas.append(float(input(f'Nota da prova {i}: ')))
        notas.sort()
media = sum(notas[1:-1])/len(notas[1:-1])
lista = [nome, idade, notas, media, media > 5]
print(('A média do aluno é: ', media))
nome = input('Digite o nome do aluno: ')
idade = input(f'Digite a idade do aluno {nome}: ')
n_provas = int(input(f'Digite o número de provas do aluno {nome}: '))
notas = []

for i in range(n_provas):
    notas.append(float(input(f'Digite a nota da prova {i+1}: ')))
    
media = sum(notas) / len(notas)
    
lista = [nome, idade, notas, media, (media > 5)]

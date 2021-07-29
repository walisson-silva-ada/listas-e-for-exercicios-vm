nome = input('Digite o nome do aluno: ')
idade = input(f'Digite a idade do aluno {nome}: ')
n_provas = int(input(f'Digite o número de provas do aluno {nome}: '))

while n_provas <= 2:
    n_provas = int(input(f'Número de provas precisa ser maior que 2. Digite novamente: '))
      
notas = []

for i in range(n_provas):
    notas.append(float(input(f'Digite a nota da prova {i+1}: ')))

notas_min_max =  list(notas)

notas_min_max.remove(min(notas_min_max))
notas_min_max.remove(max(notas_min_max))

media = sum(notas_min_max) / len(notas_min_max)
    
lista = [nome, idade, notas, media, (media > 5)]

print(lista)

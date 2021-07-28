#Q15_listas_e_for
    aluno = input('Qual o nome do aluno: ')
    idade = int(input('Qual a Idade do aluno: '))
    provas = int(input('Quantas provas o aluno fez: '))
    notas = []
    for _ in range(1,provas+1):
        notas.append(float(input(f'Nota da prova {i}: ')))
    media = sum(notas)/len(notas)
    historico_aluno = [aluno, idade, notas, media, media > 5]
    print ('Historico do Aluno',historico_aluno)
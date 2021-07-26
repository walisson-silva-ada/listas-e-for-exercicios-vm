
# Questão 15 (Listas e For)
# Considera só o que esta dentro na função main
# o que tem além disso é só boas praticas de script

def main():
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Idade do aluno: '))
    provas = int(input('Digite a quantidade de provas: '))
    notas = []
    for i in range(1,provas+1):
        notas.append(float(input(f'Nota da prova {i}: ')))
    media = sum(notas)/len(notas)
    info = [nome, idade, notas, media, media > 5]
    print(info)

if __name__ == '__main__':
    main()
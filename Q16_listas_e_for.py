
# Questão 16 (Listas e For)
# Considera só o que esta dentro na função main
# o que tem além disso é só boas praticas de script
# esse da erro se tiver menos de 3 provas 🤣
# (esqueci desse caso quando fiz 😭) 

def main():
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Idade do aluno: '))
    provas = int(input('Digite a quantidade de provas: '))
    notas = []
    for i in range(1,provas+1):
        notas.append(float(input(f'Nota da prova {i}: ')))
        notas.sort()
    media = sum(notas[1:-1])/len(notas[1:-1])
    info = [nome, idade, notas, media, media > 5]
    print(info)

if __name__=='__main__':
    main()

# Questão 21 (Funções)

def cadastrar(nome, cpf, email):
    return [nome, cpf, email]

def busca(cadastro, cpf):
    for p in cadastro:
        if cpf in p:
            return p
    print('Não encontrado')

def programa():
    cadastro = []
    option = 1
    while option != 0:
        option = int(input('Escolha a opção (0, 1, 2 ou 3): '))
        if option==0:
            print('Encerrar')
            break
        if option==1:
            print('Cadastrar')
            nome = input('Digite o nome: ')
            cpf = input('Digite o cpf: ')
            email = input('Digite o email: ')
            cadastro.append(cadastrar(nome, cpf, email))
        elif option==2:
            print('Busca')
            cpf = input('Digite o cpf: ')
            res = busca(cadastro, cpf)
            if res != None:
                print(res)
        elif option==3:
            print('Cadastro')
            for p in cadastro:
                print(p)
        else:
            continue

def main():
    programa()

if __name__=='__main__':
    main()
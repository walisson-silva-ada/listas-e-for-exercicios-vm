def cadastrar():
    cliente = []
    cliente.append(input('Nome: '))
    cliente.append(input('CPF: '))
    cliente.append(input('Email: '))
    return cliente

def buscar(clientes, cpf):
    if len(clientes) > 0:
        for c in clientes:
            if cpf in c:
                return c   
    else:
        return 'Não há clientes cadastrados'
    
    return 'Não encontrado!'

def imprimir(clientes):
    if len(clientes) > 0:
        for c in clientes:
            print(f'Nome: {c[0]} | CPF: {c[1]} | email: {c[2]}')
    else:
        print('Não há clientes cadastrados')
        
    
opcao = 1
clientes = []

while opcao != 0:
    
    print('\n')
    print('*********************************************')
    print('****** Sistema de Cadastro de Clientes ******')
    print('*********************************************')
    print('1. Cadastrar novo cliente')
    print('2. Buscar cliente por CPF')
    print('3. Listar todos os clientes cadastrados')
    print('0. Sair')

    opcao = int(input('\nDigite o número correspondente a opção deseja: '))
    
    if opcao == 1:
        cliente = cadastrar()
        clientes.append(cliente)
    
    elif opcao == 2:
        cpf = input('\nDigite o CPF que seja buscar: ')
        print(buscar(clientes, cpf))
        
    elif opcao == 3:
        imprimir(clientes)
    
    elif opcao != 0:
        print('Opção inválida! Digite novamente.')
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cadastro(nome, cpf, email):
    return [nome, cpf, email]

def busca_cpf(pessoas, cpf):
    for i in pessoas:
        if cpf in i:
            return i
    print('Ahh, não encontramos')


def programa():
    pessoas = []
    while True:        
        n = int(input('Digite sua resposta (0, 1, 2, 3):'))
        
        if n == 0:
            break
            
        elif n == 1:
            cpf = input("Cpf: ")
            nome = input("Nome: ")
            email = input("Email: ")
            pessoas.append(cadastro(nome,cpf, email))
            print(pessoas)            

        elif n == 2:
            cpf = input('Digite o cpf:')
            resultado = busca_cpf(pessoas, cpf)
            if resultado in pessoas:
                print('Eeeeee, achamos')
                
        elif n == 3:
            if len(pessoas) > 0:
                for i in pessoas:
                    print(i)

def main():
    programa()

if __name__=='__main__':
    main()
            


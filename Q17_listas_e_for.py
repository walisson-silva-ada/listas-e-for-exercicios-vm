cpf = input('Digite um CPF: ')

valida = 0
x = 10

for i in cpf[:9]:
    valida += int(i)*x
    x -= 1

if valida*10%11 == int(cpf[9]):
    valida = 0
    x = 11
    
    for i in cpf[:10]:
        valida += int(i)*x
        x -= 1
        
    if valida*10%11 == int(cpf[10]):
        print('CPF válido!')
        
    else:
        print('CPF inválido!')
        
else:
    print('CPF inválido!')


# Questão 17 (Listas e For)

def validador(cpf: str) -> bool:
    cpf = [int(d) for d in cpf]
    d = sum([cpf[i-2]*(12-i) for i in range(2,11)])*10%11
    if d != cpf[9]: return False
    d = sum([cpf[i-2]*(13-i) for i in range(2,12)])*10%11
    if d != cpf[10]: return False
    return True

def main():
    cpf = input('Digite seu cpf (somente os numeros): ')
    print('cpf válido!') if validador(cpf) else print('cpf inválido!')

if __name__=='__main__':
    main()
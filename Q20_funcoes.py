import random

def main():
    n_jogadores = int(input('Digite o número de jogadores: '))
    nomes = []
    
    for i in range(n_jogadores):
        nomes.append(input(f'Nome jogador {i+1}: '))
    
    pontuacao = dict.fromkeys(nomes, 0)
    ativos = dict.fromkeys(nomes, True)
        
    baralho = cria_baralho()
    
    while True in ativos.values():
        
        jogadores_ativos = [a for a, ativo in ativos.items() if ativo]
        
        for jogador in jogadores_ativos:
            ativos, pontuacao = jogada(jogador, ativos, pontuacao, baralho)
    
    print(f'O(s) vencedor(es) foi(foram) {verifica(pontuacao)[0]} com {verifica(pontuacao)[1]} pontos!')
    
        
def cria_baralho():
    baralho = [i for i in range(1, 11)] # indo de Ás (valendo 1) até 10
    baralho += [10, 10, 10] # mais Valete, Dama e Rei (valendo 10 também)
    baralho *= 4 # multiplicando por 4 para representar cada naipe
    return baralho

def jogada(nome, ativo, pontuacao, baralho):
    if pontuacao[nome] < 21:
        resposta = input(f'{nome}, sua pontuação é de {pontuacao[nome]}, deseja comprar uma carta? (Digite sim ou não): ') 
        if resposta.upper() == 'SIM':
            pontuacao[nome] += sorteia(baralho)
            print(f'{nome}, sua pontuação agora é de {pontuacao[nome]}')
        else:
            ativo[nome] = False
    else:
        ativo[nome] = False
        
    return ativo, pontuacao
        
def sorteia(baralho):
    numero_sorteado = random.randint(0,51)
    # print(f'O número sorteado foi {numero_sorteado} que corresponde a carta {baralho[numero_sorteado]}')
    return baralho[numero_sorteado]

def verifica(pontuacao):
    maior = 0
    nome = []

    for i in pontuacao:
        if maior < pontuacao[i] and pontuacao[i] <= 21:
            maior = pontuacao[i]
            nome = [i]
        elif maior == pontuacao[i]:
            nome.append(i)

        return nome, maior

if __name__ == '__main__':
    main()

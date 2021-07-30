from random import randint

def iniciar_jogo():
    return 4*(list(range(1,11))+[10,10,10])

def baralho_cartas(baralho):
    i = randint(0, len(baralho))
    valor = baralho.pop(i)
    print(f'carta comprada vale {valor}!\n')
    return valor

def dados_para_jogo(nome, jogadores, baralho):
    print(f'{nome}, agora é sua vez')
    ans = input('Deseja comprar um carta? (S / N): ')
    while ans not in ("N", "S"):
        ans = input('S ou N!')
    if ans == "N":
        jogadores[nome]['status'] = False
    elif ans == "S":
        jogadores[nome]['cards'].append(get_card(baralho))
        total = sum(jogadores[nome]['cards'])
        if total > 21:
            jogadores[nome]['status'] = False
            print(f'{nome} ultrapassou 21 e está fora!\n')

def quem_vence(jogadores):
    ganhador = 'Ninguém'
    maior = 0
    for jogador in jogadores.keys():
        total = sum(jogadores[jogador]['cards'])
        if total < 21 and total > maior:
            ganhador = jogador
            maior = total
    print(f'O vencedor é {ganhador}!')

def jogando_cartas():
    n_jogadores = int(input('Digite o número de jogadores: '))
    baralho = iniciar_jogo()
    jogadores = {}
    for j in range(n_jogadores):
        nome = input(f'Nome do jogador {j+1}: ')
        while nome in jogadores.keys() and jogadores != {}:
            nome = input(f'Jogador {j}, escolha outro nome: ')
        jogadores[nome] = {'status':True,'cards':[]}
    while any([p['status'] for p in jogadores.values()]):
        for jogador in jogadores.keys():
            if jogadores[jogador]['status']:
                dados_para_jogo(jogador, jogadores, baralho)
    quem_vence(jogadores)

def main():
    jogando_cartas()

if __name__=='__main__':
    main()

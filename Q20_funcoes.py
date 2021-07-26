# Questão 20 (Funções)

from random import randint

def deck():
    return 4*(list(range(1,11))+[10,10,10])

def get_card(baralho):
    i = randint(0, len(baralho))
    valor = baralho.pop(i)
    print(f'carta comprada vale {valor}!\n')
    return valor

def deal_card(nome, players, baralho):
    print(f'{nome}, agora é seu turno')
    ans = input('Deseja comprar um carta? (S / N): ')
    while ans not in ("N", "S"):
        ans = input('S ou N!')
    if ans == "N":
        players[nome]['status'] = False
    elif ans == "S":
        players[nome]['cards'].append(get_card(baralho))
        total = sum(players[nome]['cards'])
        if total > 21:
            players[nome]['status'] = False
            print(f'{nome} ultrapassou 21 e está fora!\n')

def win_condition(players):
    winner = 'Ninguém'
    maior = 0
    for player in players.keys():
        total = sum(players[player]['cards'])
        if total < 21 and total > maior:
            winner = player
            maior = total
    print(f'O vencedor é {winner}!')

def game_on():
    n_players = int(input('Digite o número de jogadores: '))
    baralho = deck()
    players = {}
    for j in range(n_players):
        nome = input(f'Nome do jogador {j+1}: ')
        while nome in players.keys() and players != {}:
            nome = input(f'Jogador {j}, escolha outro nome: ')
        players[nome] = {'status':True,'cards':[]}
    while any([p['status'] for p in players.values()]):
        for player in players.keys():
            if players[player]['status']:
                deal_card(player, players, baralho)
    win_condition(players)

def main():
    game_on()

if __name__=='__main__':
    main()

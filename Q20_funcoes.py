#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

def baralho_total():
    return 4*(list(range(1,11))+[10,10,10])

def pegar_carta(baralho):
    i = randint(0, len(baralho))
    carta = baralho.pop(i)
    print(f'A carta vale {carta}!\n')
    return carta

def jogo(nome, jogadores, baralho):
    print(f'{nome}, é seu turno')
    comprar = input('Deseja comprar uma carta? (S / N): ')
    while comprar not in ("N", "S"):
        comprar = input('S ou N!')
    if comprar == "N":
        jogador[nome]['status'] = False
    elif comprar == "S":
        jogadores[nome]['cartas'].append(pegar_carta(baralho))
        total = sum(jogadores[nome]['cartas'])
        if total > 21:
            jogadores[nome]['status'] = False
            print(f'{nome} ultrapassou 21 e está fora!\n')

def ganhar(jogadores):
    vencedor = 'Ninguém'
    maior = 0
    for jogador in jogadores.keys():
        total = sum(jogadores[jogador]['cards'])
        if total < 21 and total > maior:
            vencedor = jogador
            maior = total
    print(f'O vencedor é {vencedor}!')

def inicio_jogo():
    n_jogadores = int(input('Digite o número de jogadores: '))
    baralho = baralho_total()
    jogadores = {}
    for j in range(n_jogadores):
        nome = input(f'Nome do jogador {j+1}: ')
        while nome in jogadores.keys() and jogadores != {}:
            nome = input(f'Jogador {j}, escolha outro nome: ')
        jogadores[nome] = {'status':True,'cards':[]}
    while any([p['status'] for p in jogadores.values()]):
        for jogador in jogadores.keys():
            if jogadores[jogador]['status']:
                jogo(jogador, jogadores, baralho)
    ganhar(jogadores)

def inicio():
    inicio_jogo()

if __name__=='__inicio__':
    inicio()


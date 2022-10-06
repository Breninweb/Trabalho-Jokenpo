#Criar um jogo de Jokempo, tendo 3 modos de jogo:

#1. Jogador vs Jogador

#2. Jogador vs Computador

#3. Computador vs Computador

import random

rodada = 0

print("1. Jogador vs Jogador")
print("2. Jogador vs Computador")
print("3. Computador vs Computador")
modoJogo = int(input("Escolha o modo de jogo: "))


if modoJogo == 1:
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    Jogador1 = int(input("Jogada do jogador 1: "))
    if Jogador1 == 1:
        print("Pedra")
    elif Jogador1 == 2:
        print("Papel")
    elif Jogador1 == 3:
        print("Tesoura")
    else:
        print("Jogada não existe")

    print("")
    Jogador2 = int(input("Jogada do jogador 2: "))
    if Jogador2 == 1:
        print("Pedra")
    elif Jogador2 == 2:
        print("Papel")
    elif Jogador2 == 3:
        print("Tesoura")



while modoJogo == 1 and rodada == 0:
    if Jogador1 == 1 and Jogador2 == 3:
        print("Jogador 1 venceu")
    elif Jogador1 == Jogador2:
        print("Empate")
    else:
        print("Jogador 2 venceu")
        rodada = 1
    break

    if Jogador1 == 2 and Jogador2 == 1:
        print("Jogador 1 venceu")
    elif Jogador1 == Jogador2:
        print("Empate")
    else:
        print("Jogador 2 venceu")
        rodada = 1
    break

    if Jogador1 == 3 and Jogador2 == 2:
        print("Jogador 1 venceu")
    elif Jogador1 == Jogador2:
        print("Empate")
    else:
        print("Jogador 2 venceu")
        rodada = 1
    break

#    if rodada == 1:
#        continuar = int(input("Deseja jogar novamente?"))
#        print("1. Jogar novamente")
#        print("2. Desistir")
#        if continuar == 1:
#            rodada = 0
#        else:
#            print("Desligando")
#        break

if modoJogo == 2:
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    Jogador1 = int(input("Jogada do jogador 1: "))
    Computador1 = random.randint(1, 3)
    if Jogador1 == 1:
        print("Pedra")
    elif Jogador1 == 2:
        print("Papel")
    elif Jogador1 == 3:
        print("Tesoura")
    else:
        print("Jogada não existe")
    if Computador1 == 1:
        print("Computador escolheu Pedra")
    elif Computador1 == 2:
        print("Computador escolheu Papel")
    elif Computador1 == 3:
        print("Computador escolheu Tesoura")


while modoJogo == 2 and rodada == 0:
    if Jogador1 == 1 and Computador1 == 3:
        print("Jogador venceu")
    elif Jogador1 == Computador1:
        print("Empate")
    elif Jogador1 == 1 and Computador1 == 2:
        print("Computador venceu")
    break

    if Jogador1 == 2 and Computador1 == 1:
        print("Jogador venceu")
    elif Jogador1 == Computador1:
        print("Empate")
    elif Jogador1 == 2 and Computador1 == 3:
        print("Computador venceu")
    break

    if Jogador1 == 3 and Computador1 == 2:
        print("Jogador venceu")
    elif Jogador1 == Computador:
        print("Empate")
    elif Jogador1 == 3 and Computador1 == 1:
        print("Computador venceu")
    break

if modoJogo == 3:
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    Computador1 = random.randint(1, 3)
    Computador2 = random.randint(1, 3)
    if Computador1 == 1:
        print("Computador 1 escolheu Pedra")
    elif Computador1 == 2:
        print("Computador 1 escolheu Papel")
    elif Computador1 == 3:
        print("Computador 1 escolheu Tesoura")

    if Computador2 == 1:
        print("Computador 2 escolheu Pedra")
    elif Computador2 == 2:
        print("Computador 2 escolheu Papel")
    elif Computador2 == 3:
        print("Computador 2 escolheu Tesoura")


while modoJogo == 3 and rodada == 0:
    if Computador1 == 1 and Computador2 == 3:
        print("Computador 1 venceu")
    elif Computador1 == Computador2:
        print("Empate")
    elif Computador1 == 1 and Computador2 == 2:
        print("Computador 2 venceu")
    break

    if Computador1 == 2 and Computador2 == 1:
        print("Computador 1 venceu")
    elif Computador1 == Computador2:
        print("Empate")
    elif Computador1 == 2 and Computador2 == 3:
        print("Computador 2 venceu")
    break

    if Computador1 == 3 and Computador2 == 2:
        print("Computador 1 venceu")
    elif Computador1 == Computador2:
        print("Empate")
    elif Computador1 == 3 and Computador2 == 1:
        print("Computador 2 venceu")
    break

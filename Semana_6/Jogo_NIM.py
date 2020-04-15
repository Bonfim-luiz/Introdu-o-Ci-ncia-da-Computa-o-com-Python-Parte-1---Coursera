def usuario_escolhe_jogada (n,m):
    entrada=int(input("Quantas peças você vai tirar? "))
    while entrada>m or entrada>n or entrada<1:
        print("Oops! Jogada inválida! Tente de novo.")
        entrada=int(input("Quantas peças você vai tirar? "))
    entrada
    return entrada

def computador_escolhe_jogada(n,m):
    a=1
    indicador=False
    while a<m and not indicador:
        if (n-a)%(m+1)==0:
            indicador=True
        else:
            a=a+1
    return a

def partida():
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    if n%(m+1)==0:
        comp_inicia=False
        print("")
        print("Voce começa!")
        print("")
    else:
        comp_inicia=True
        print("")
        print("Computador começa!")
    while n>0:
        if comp_inicia:
            retirada_pc=computador_escolhe_jogada(n,m)
            n=n-retirada_pc
            if retirada_pc == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", retirada_pc, "peças.")
            comp_inicia=False
        else:
            retirada_usuario=usuario_escolhe_jogada (n,m)
            n=n-retirada_usuario
            if retirada_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print("Voce tirou", retirada_usuario,"peças.")
            comp_inicia=True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print("")
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()
    print('Fim do jogo! O computador ganhou!')

def campeonato():
    n_partida = 1
    while n_partida <= 3:
        print()
        print("**** Rodada", n_partida, "****")
        print()
        partida()
        n_partida = n_partida + 1
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você 0 X 3 Computador")
    
print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
print("1 - para jogar uma partida isolada")
n=int(input("2 - para jogar um campeonato "))
if n == 2:
    print("")
    print("Voce escolheu um campeonato!")
    print("")
    campeonato()
else:
    print("")
    print("Voce escolheu uma partida isolada!")
    print("")
    partida()

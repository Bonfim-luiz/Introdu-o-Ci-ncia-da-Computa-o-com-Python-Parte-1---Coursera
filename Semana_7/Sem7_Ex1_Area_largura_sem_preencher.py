#Area e largura sem preenchimento
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
preenche = "#"

def ret(largura, altura, preenche):

    cheia = preenche * largura
    if largura > 2:
        vazia = preenche + (" " * (largura - 2)) + preenche
    else:
        vazia = cheia
#Primeira linha
    if altura >= 1:
        print(cheia)
#Linhas sem preenchimento
    while altura-2>0:
        print(vazia)
        altura=altura-1
#Ultima linha
    if altura >= 2:
        print(cheia)

ret(largura, altura, preenche)

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e 
    devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das 
    sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve 
    uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve 
    uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e 
    devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e 
    devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    soma = 0
    n = 0
    c = as_a + as_b
    while n < 6:
        soma = soma + abs(c[n] - c[n + 6])
        n = n + 1
    return (soma/6)

def texto_frase(texto):
    '''Essa funcao recebe um texto e 
    devolve uma lista com as frases'''
    x = separa_sentencas(texto)
    z = []
    for i in x:
        z = z + separa_frases(i) 
    return z

def frase_palavra(texto):
    '''Essa funcao recebe um texto e 
    devolve uma lista com as palavras'''
    x = texto_frase(texto)
    z = []
    for i in x:
        z = z + separa_palavras(i)
    return z

def calcula_assinatura(texto):
    # Tamanho médio de palavra
    x = frase_palavra(texto)
    resultado = []
    soma=0
    for i in x:
        soma=soma+len(i)
    wal = soma/(len(x))
    resultado.append(wal)
    
    # Relação Type-Token
    dif = n_palavras_diferentes(x)
    ttr = dif/len(x)
    resultado.append(ttr)
    
    # Razão Hapax Legomana
    unica = n_palavras_unicas(x)
    hlr = unica/len(x)
    resultado.append(hlr)
    
    # Tamanho médio de sentença
    lista_setenca = separa_sentencas(texto)
    soma_setenca = 0
    for i in lista_setenca:
        soma_setenca = soma_setenca + len(i)
    sal = soma_setenca/(len(lista_setenca))
    resultado.append(sal)
    
    # Complexidade de sentença
    qtd_frase = len(texto_frase(texto))
    qtd_setenca = len(lista_setenca)
    sac = qtd_frase/qtd_setenca
    resultado.append(sac)
    
    # Tamanho médio de frase
    lista_frase = texto_frase(texto)
    soma_frase = 0
    for i in lista_frase:
        soma_frase = soma_frase + len(i)
    pal = soma_frase/(len(lista_frase))
    resultado.append(pal)
    
    return resultado

def minimo_elemento(lista):
    for i in lista:
        n_min = min(lista)
        n_pos = lista.index(n_min)
    return n_pos

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma 
    assinatura ass_cp e deve devolver o numero (1 a n) do texto 
    com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinatura_entrada = ass_cp
    lista_textos = textos
    comparacao = []
    for i in lista_textos:
        intermed = calcula_assinatura(i)
        calculo = compara_assinatura(intermed,assinatura_entrada)
        comparacao.append(calculo)
    resultado_final = minimo_elemento(comparacao)+1
    return resultado_final
   
ass_cp = le_assinatura()
textos = le_textos()
resultado_final1 = avalia_textos(textos, ass_cp)
print("O autor do texto",resultado_final1,"está infectado com COH-PIAH")

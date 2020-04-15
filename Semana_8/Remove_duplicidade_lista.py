def remove_repetidos(lista):
    novo=[]
    for i in lista:
        if i not in novo:
            novo.append(i)
    novo.sort()
    return novo

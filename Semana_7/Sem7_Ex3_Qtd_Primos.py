#Quantidade de primos entre 2 e N
def éPrimo(x):
    fator=2
    if x==2:
        return True
    while x%fator!=0 and fator<=x/2:
        fator=fator+1
    if x%fator==0:
        return False
    else:
        return True

def n_primos(n): 
    contagem=0
    while n>1:
        if éPrimo(n):
            contagem=contagem+1
        n=n-1
    return contagem

def ehPrimo(k):   
    entrada=k
    n=2
    primo=True
    while n<entrada and primo:
        if entrada%n==0:
            primo=False
        n=n+1
    if primo:
        return k
    else:
        return 0

def maior_primo(x):
    while x>1:
        if ehPrimo(x) > 0:
            return x
        x=x-1

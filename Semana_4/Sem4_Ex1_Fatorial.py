entrada=int(input("Digite o valor de n: "))
n=1
fatorial=1
indicador=True
while n<=entrada and indicador:
    if n == entrada:
        fatorial=fatorial*n
        indicador=False
    else:
        fatorial=fatorial*n
    n=n+1
print(fatorial)

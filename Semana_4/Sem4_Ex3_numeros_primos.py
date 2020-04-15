entrada=int(input("Digite um número inteiro: "))
n=2
primo=True
while n<entrada and primo:
    if entrada%n==0:
        primo=False
    n=n+1
if primo:
    print("primo")
else:
    print("não primo")

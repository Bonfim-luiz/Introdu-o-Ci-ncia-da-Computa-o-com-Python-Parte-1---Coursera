entrada=int(input("Digite um número: "))
lista=[]
while entrada!=0:
    lista.append(entrada)
    entrada=int(input("Digite um número: "))

tam=len(lista)
for i in lista:
    print(lista[tam-1])
    tam=tam-1

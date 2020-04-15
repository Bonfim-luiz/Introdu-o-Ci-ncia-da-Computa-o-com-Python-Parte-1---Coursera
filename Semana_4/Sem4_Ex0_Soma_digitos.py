numero=int(input("Digite um número inteiro: "))
soma=0
while numero//10 >= 0:
        resto = numero%10
        soma = soma + resto
        if numero == 0:
            numero=-1
        else:
            numero = numero//10
print(soma)

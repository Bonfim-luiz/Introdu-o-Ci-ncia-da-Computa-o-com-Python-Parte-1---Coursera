#Soma das Hipotenusas
import math
def éhipotenusa(n):
    i=1
    while i<n:
        j=1
        while j<n:
            hipotenusa = int(math.sqrt((i ** 2) + (j ** 2)))
            if (hipotenusa > i) and (hipotenusa > j) and (hipotenusa < (i + j)):
                if ((i ** 2) + (j ** 2) == hipotenusa ** 2):
                    if(hipotenusa == n):
                        return hipotenusa               
            j=j+1
        i=i+1
    return 0

def soma_hipotenusas(n):
    soma=0
    while n>0:
        resultado=éhipotenusa(n)
        if resultado!=0:
            soma=soma+resultado
        n=n-1
    return soma

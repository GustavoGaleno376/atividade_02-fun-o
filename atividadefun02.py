# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
num=int(input("digite um numero"))
def par_impar(num):
    pareimp=num % 2
    if pareimp==0:
        return "numero par"
    else:
        return "numero ímpar"
    

mani=par_impar(num)
print(mani)
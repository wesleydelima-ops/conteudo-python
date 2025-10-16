numero = int(input("digite um numero inteiro aleatório:"))

resto = numero % 2

if resto == 1:
    print("o valor",numero,"é ímpar")
else:
    print("o valor",numero,"é par")
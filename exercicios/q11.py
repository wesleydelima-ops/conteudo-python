# Solicitar dois números inteiros
num_inteiro1 = int(input("Digite o primeiro número inteiro: "))
num_inteiro2 = int(input("Digite o segundo número inteiro: "))

# Solicitar um número real
num_real = float(input("Digite um número real: "))

# Exemplo de operação: somar os dois inteiros e subtrair o real
resultado_soma_subtracao = (num_inteiro1 + num_inteiro2) - num_real

# Exibir os resultados
print(f"Os números inteiros digitados foram: {num_inteiro1} e {num_inteiro2}")
print(f"O número real digitado foi: {num_real}")
print(f"Resultado da soma dos inteiros menos o real: {resultado_soma_subtracao}")
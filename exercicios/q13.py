# Solicita ao usuário a quantidade em gigabytes
gb = float(input("Digite a quantidade em Gigabytes (GB): "))

# Define o fator de conversão (1 TB = 1024 GB)
fator_conversao = 1024

# Realiza a conversão de GB para TB
tb = gb / fator_conversao

# Imprime o resultado
print(f"{gb} GB é igual a {tb:.4f} TB")
# Define o limite de peso e o valor da multa
limite_peso = 50
valor_multa_por_quilo = 4.00

# Pede ao usuário para inserir o peso dos peixes
peso_peixes = float(input("Digite o peso total dos peixes (em kg): "))

# Calcula o excesso de peso
if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    multa = excesso * valor_multa_por_quilo
else:
    excesso = 0
    multa = 0

# Imprime os resultados com mensagens adequadas
print(f"\n--- Resultado da Pesagem ---")
print(f"Peso total dos peixes: {peso_peixes:.2f} kg")

if excesso > 0:
    print(f"Você excedeu o limite de {limite_peso} kg.")
    print(f"Quilos excedentes: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")
else:
    print(f"Você não excedeu o limite de {limite_peso} kg.")
    print("Não há multa a pagar.")
# Solicita a entrada do usuário
valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Define os percentuais de desconto
percentual_ir = 0.11
percentual_inss = 0.08
percentual_sindicato = 0.05

# Calcula os valores dos descontos
desconto_ir = salario_bruto * percentual_ir
desconto_inss = salario_bruto * percentual_inss
desconto_sindicato = salario_bruto * percentual_sindicato

# Calcula o total dos descontos
total_descontos = desconto_ir + desconto_inss + desconto_sindicato

# Calcula o salário líquido
salario_liquido = salario_bruto - total_descontos

# Mostra os resultados
print(f"\n--- Holerite ---")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto Imposto de Renda (11%): R$ {desconto_ir:.2f}")
print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
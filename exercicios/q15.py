# Solicita o valor que o usuário ganha por hora
ganho_por_hora = float(input("Quanto você ganha por hora? "))

# Solicita o número de horas trabalhadas no mês
horas_trabalhadas = float(input("Quantas horas você trabalhou neste mês? "))

# Calcula o salário bruto
salario_bruto = ganho_por_hora * horas_trabalhadas

# Calcula os descontos
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
total_descontos = desconto_ir + desconto_inss + desconto_sindicato

# Calcula o salário líquido
salario_liquido = salario_bruto - total_descontos

# Exibe os resultados
print(f"\n--- Resumo do Salário ---")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto IR (11%): R$ {desconto_ir:.2f}")
print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
print(f"Total de Descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
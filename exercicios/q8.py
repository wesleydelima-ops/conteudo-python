valor_por_hora = float(input("Qual é o valor do seu salário por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalhou neste mês? "))
salario_bruto = valor_por_hora * horas_trabalhadas
print(f"O seu salário bruto é: R$ {salario_bruto:.2f}")
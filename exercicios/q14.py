limite_peso = 50
valor_multa_por_kg = 4.00

peso_peixe = float(input("Digite o peso total dos peixes (em kg): "))
if peso_peixe > limite_peso:
    excedente = peso_peixe - limite_peso
    multa = excedente * valor_multa_por_kg


    print("houveram",excedente,"kg de peixe a mais do permitido")
    print("O valor da multa é R$",multa)
else:
    print("Não foi maior do que o permitido.")
import math

area_pintar = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area_pintar / 3

latas_comprar = math.ceil(litros_necessarios / 18)

preco_total = latas_comprar * 80

print(f"Serão necessárias {latas_comprar} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")
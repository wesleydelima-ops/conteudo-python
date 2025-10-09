def celsius_para_fahrenheit(celsius):
  """Converte temperatura de Celsius para Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Exemplo de uso:
temperatura_celsius = 30
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")
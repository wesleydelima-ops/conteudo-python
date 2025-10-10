# Solicita o tamanho do arquivo em MB
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo em MB: "))

# Solicita a velocidade da internet em Mbps
velocidade_link_mbps = float(input("Digite a velocidade do link de internet em Mbps: "))

# Calcula o tempo de download em segundos
# Multiplica o tamanho do arquivo por 8 para converter de MB para megabits
# Divide pelo velocidade do link em Mbps para obter o tempo em segundos
tempo_segundos = (tamanho_arquivo_mb * 8) / velocidade_link_mbps

# Converte o tempo de segundos para minutos dividindo por 60
tempo_minutos = tempo_segundos / 60

# Exibe o resultado
print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.")
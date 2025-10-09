def converter_gb_para_mb(gb, tipo_conversao="binario"):
    """
    Converte gigabytes para megabytes.

    Args:
        gb (float): A quantidade de gigabytes.
        tipo_conversao (str): "binario" para usar 1024, ou "decimal" para usar 1000.

    Returns:
        float: O valor em megabytes.
    """
    if tipo_conversao.lower() == "binario":
        # Conversão binária (1 GB = 1024 MB)
        fator = 1024
    elif tipo_conversao.lower() == "decimal":
        # Conversão decimal (1 GB = 1000 MB)
        fator = 1000
    else:
        return "Tipo de conversão inválido. Use 'binario' ou 'decimal'."

    mb = gb * fator
    return mb


# Exemplo de uso (entrada do usuário):
try:
    gb_entrada = float(input("Digite a quantidade de Gigabytes (GB) para converter: "))
    tipo = input("Qual tipo de conversão deseja? (binario/decimal): ").strip().lower()

    resultado_mb = converter_gb_para_mb(gb_entrada, tipo)

    if isinstance(resultado_mb, float):
        print(f"{gb_entrada} GB equivalem a {resultado_mb} MB (na conversão {tipo})")
    else:
        print(resultado_mb)

except ValueError:
    print("Por favor, insira um número válido para os Gigabytes.")
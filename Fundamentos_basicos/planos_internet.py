def recomendar_plano(consumo):
    # Verifica o consumo médio mensal e recomenda um plano adequado
    if consumo <= 10:
        print("Plano Essencial Fibra - 50Mbps")
    elif consumo <= 19:
        print("Plano Prata Fibra - 100Mbps")
    elif consumo <= 21:
        print("Plano Premium Fibra - 300Mbps")
    else:
        print("Nenhum plano encontrado para o consumo inserido.")

# Solicita ao usuário que insira o consumo médio mensal de dados
consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado
recomendar_plano(consumo)

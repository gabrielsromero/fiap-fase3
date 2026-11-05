from dados import historico

def media(lista):
    return sum(lista) / len(lista)

def calcular_reta(lista_x, lista_y):
    media_x = media(lista_x)
    media_y = media(lista_y)

    soma_cima = 0     # soma de (x - x̄)·(y - ȳ)
    soma_baixo = 0    # soma de (x - x̄)²

    for x, y in zip(lista_x, lista_y):
        soma_cima = soma_cima + (x - media_x) * (y - media_y)
        soma_baixo = soma_baixo + (x - media_x) ** 2

    b1 = soma_cima / soma_baixo
    b0 = media_y - b1 * media_x
    return b1, b0

def prever(vento, b1, b0):
    return b0 + b1 * vento

# listas do histórico (ficam fora do teste porque o grafico.py e o main.py usam)
ventos = []
eolicas = []
for dia in historico:
    ventos.append(dia["vento"])
    eolicas.append(dia["ge_eolica"])

if __name__ == "__main__":
    b1, b0 = calcular_reta([8, 10, 12], [20, 25, 30])
    print("Exemplo do enunciado, vento 11:", prever(11, b1, b0))

    b1, b0 = calcular_reta(ventos, eolicas)
    print("Reta do histórico: b1 =", round(b1, 2), "b0 =", round(b0, 2))
    print("Previsão para vento 11:", round(prever(11, b1, b0), 2))

    b1_val, b0_val = calcular_reta(ventos[:6], eolicas[:6])
    previsto = prever(ventos[6], b1_val, b0_val)
    print("Dia 7 previsto:", round(previsto, 2), "real:", eolicas[6])
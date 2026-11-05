import matplotlib.pyplot as plt
from previsao import calcular_reta, prever, ventos, eolicas

b1, b0 = calcular_reta(ventos, eolicas)

# pontos reais do histórico
plt.scatter(ventos, eolicas, label="Dados reais (7 dias)")

# reta da regressão, do menor ao maior vento
x_reta = [min(ventos), max(ventos)]
y_reta = [prever(x, b1, b0) for x in x_reta]
plt.plot(x_reta, y_reta, label="Reta: y = -0,13 + 2,52x")

plt.xlabel("Velocidade do vento (m/s)")
plt.ylabel("Energia eólica (MWh)")
plt.title("Regressão linear: vento x energia eólica")
plt.legend()
plt.grid(True)
plt.savefig("grafico_regressao.png")
print("Gráfico salvo")
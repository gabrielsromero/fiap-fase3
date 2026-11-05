from dados import historico, sistemas
from organizacao import sensores_do_sistema, sistema_do_sensor
from decisoes import geracao_total, avaliar_dia
from previsao import media, calcular_reta, prever, ventos, eolicas
from energia import analisar_energia

print("=== SISTEMA DA COLÔNIA AURORA ===")

# 1. Organização dos dados: navegação entre sistemas e sensores
print("\n--- 1. Sistemas e sensores ---")
for nome_sistema in sistemas:
    print(nome_sistema, "->", sensores_do_sistema(nome_sistema))
print("O sensor 'vento' pertence ao:", sistema_do_sensor("vento"))

# 2. Decisões: regras com prioridade, dia a dia
print("\n--- 2. Decisões automáticas (7 dias) ---")
for dia in historico:
    print("Dia", dia["dia"], ":", avaliar_dia(dia))

# 3. Previsão: regressão linear vento -> energia eólica
print("\n--- 3. Previsão (regressão linear) ---")
b1, b0 = calcular_reta(ventos, eolicas)
print("Reta: energia =", round(b0, 2), "+", round(b1, 2), "x vento")

# 4. Análise do uso de energia: geração x consumo
print("\n--- 4. Análise de energia (7 dias) ---")
for dia in historico:
    geracao = geracao_total(dia)
    print("Dia", dia["dia"], ": geração", geracao, "| consumo", dia["consumo"], "|", analisar_energia(geracao, dia["consumo"]))

# 5. Integração: previsão para amanhã usando a reta + análise de energia
print("\n--- 5. Previsão para amanhã ---")
solares = []
consumos = []
for dia in historico:
    solares.append(dia["ge_solar"])
    consumos.append(dia["consumo"])

solar_media = media(solares)
consumo_medio = media(consumos)

for vento_amanha in [7, 11, 15]:
    eolica_prevista = prever(vento_amanha, b1, b0)
    geracao_prevista = eolica_prevista + solar_media
    print("Vento", vento_amanha, "m/s: geração prevista", round(geracao_prevista, 2),
          "| consumo médio", round(consumo_medio, 2), "|", analisar_energia(geracao_prevista, consumo_medio))
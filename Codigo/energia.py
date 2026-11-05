from dados import historico
from decisoes import geracao_total

def analisar_energia(geracao, consumo):
    saldo = geracao - consumo

    if saldo < 0:
        return "ALERTA: consumo maior que geração"
    elif saldo > 10:
        return "SUGESTÃO: armazenar energia excedente"
    else:
        return "Energia em equilíbrio"

if __name__ == "__main__":
    print(analisar_energia(40, 70))
    print(analisar_energia(80, 30))
    for dia in historico:
        print(dia["dia"], analisar_energia(geracao_total(dia), dia["consumo"]))
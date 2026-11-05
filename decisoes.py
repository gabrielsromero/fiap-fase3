from dados import historico

def geracao_total(dia):
    return dia["ge_solar"] + dia["ge_eolica"]

def avaliar_dia(dia):
    total = geracao_total(dia)

    if dia["temp_int"] <= 15 and total < dia["consumo"]:
        return "ALERTA CRÍTICO: frio com falta de energia, desligar módulos não essenciais e manter aquecimento"
    elif dia["temp_int"] <= 15:
        return "ALERTA: temperatura interna baixa, ativar aquecimento"
    elif total < dia["consumo"] and dia["vento"] < 8:
        return "ALERTA: falta energia e o vento está fraco, reduzir consumo"
    elif total < dia["consumo"]:
        return "AVISO: consumo acima da geração"
    else:
        return "Sistema normal"

if __name__ == "__main__":
    for dia in historico:
        print(dia["dia"], avaliar_dia(dia))
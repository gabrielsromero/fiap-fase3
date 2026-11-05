from dados import sistemas, sensores

def sensores_do_sistema(nome_sistema):
    return sistemas[nome_sistema]

def sistema_do_sensor(nome_sensor):
    return sensores[nome_sensor]["sistema"]

if __name__ == "__main__":
    print(sensores_do_sistema("Sistema Energetico"))
    print(sistema_do_sensor("vento"))
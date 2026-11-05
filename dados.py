
sensores = {
    "ge_solar":  {"nome": "Geração Solar", "sistema": "Sistema Energético", "unidade": "MWh"},
    "ge_eolica": {"nome": "Geração Eólica", "sistema": "Sistema Energético", "unidade": "MWh"},
    "temp_int": {"nome": "Temperatura Interna", "sistema": "Sistema Ambiental", "unidade": "°C"},
    "temp_ext": {"nome": "Temperatura Externa", "sistema": "Sistema Ambiental", "unidade": "°C"},
    "vento": {"nome": "Velocidade do vento", "sistema": "Sistema Ambiental", "unidade": "m/s"},
    "consumo": {"nome": "Consumo dos módulos", "sistema": "Sistema Operacional", "unidade": "MWh"},

}

historico = [
    {"dia": 1, "vento": 6,  "ge_eolica": 15, "ge_solar": 30, "consumo": 52, "temp_int": 18},
    {"dia": 2, "vento": 8,  "ge_eolica": 20, "ge_solar": 28, "consumo": 40, "temp_int": 17},
    {"dia": 3, "vento": 10, "ge_eolica": 25, "ge_solar": 25, "consumo": 50, "temp_int": 16},
    {"dia": 4, "vento": 12, "ge_eolica": 30, "ge_solar": 22, "consumo": 70, "temp_int": 15},
    {"dia": 5, "vento": 7,  "ge_eolica": 18, "ge_solar": 31, "consumo": 30, "temp_int": 19},
    {"dia": 6, "vento": 9,  "ge_eolica": 22, "ge_solar": 27, "consumo": 55, "temp_int": 17},
    {"dia": 7, "vento": 13, "ge_eolica": 33, "ge_solar": 20, "consumo": 45, "temp_int": 14},
]

sistemas = {
    "Sistema Energético": ["ge_solar", "ge_eolica"],
    "Sistema Ambiental": ["temp_int", "temp_ext", "vento"],
    "Sistema Operacional": ["consumo"]
}


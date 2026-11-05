# Sistema da Colônia Aurora (Fase 3 - FIAP)

Projeto da Atividade Integradora da Fase 3 de Ciência da Computação da FIAP: **"A Aurora Estabelece os Primeiros Sistemas da Colônia"**.

**Aluno:** Gabriel Romero · **RM:** 575479

## O que o sistema faz
É um sistema simples em Python que representa a colônia em Marte. Ele:

1. **Organiza os dados** dos sensores (energia, consumo e clima) e os sistemas da colônia de forma hierárquica, com navegação entre eles.
2. **Toma decisões automáticas** com regras de prioridade (o suporte à vida vem primeiro).
3. **Prevê a energia eólica** a partir da velocidade do vento, usando regressão linear (mínimos quadrados).
4. **Analisa o uso de energia**, comparando geração e consumo, e sugere o que fazer (reduzir consumo ou armazenar o excedente).

Também junta a previsão com a análise: com o vento esperado pra amanhã, o sistema avisa antes se vai faltar ou sobrar energia.

## Arquivos
| Arquivo | O que faz |
| ------- | --------- |
| `dados.py` | guarda os dados: sensores, histórico de 7 dias e sistemas |
| `organizacao.py` | navegação: do sistema pro sensor e do sensor pro sistema |
| `decisoes.py` | geração total do dia e as 4 regras de decisão com prioridade |
| `previsao.py` | média, cálculo da reta (regressão linear) e previsão |
| `energia.py` | saldo de energia (geração − consumo) e a sugestão |
| `main.py` | junta tudo e mostra o resultado |
| `grafico.py` | opcional, gera o gráfico da regressão pro relatório (usa matplotlib) |

O sistema (`main.py` e os arquivos que ele usa) não precisa de nenhuma biblioteca de fora, só Python.

## Como rodar
Precisa de Python 3 instalado. Na pasta do projeto:

```
python main.py
```

Pra rodar os testes de cada parte separada, é só rodar o arquivo sozinho (ex.: `python decisoes.py`).

Pra gerar o gráfico (opcional):

```
pip install matplotlib
python grafico.py
```

## Exemplo de entrada e saída

**Entrada:** o histórico de 7 dias que está no `dados.py`, por exemplo o dia 4:

```
{"dia": 4, "vento": 12, "ge_eolica": 30, "ge_solar": 22, "consumo": 70, "temp_int": 15}
```

e o vento esperado pra amanhã (7, 11 e 15 m/s no exemplo).

**Saída** (`python main.py`):

```
=== SISTEMA DA COLÔNIA AURORA ===

--- 1. Sistemas e sensores ---
Sistema Energetico -> ['ge_solar', 'ge_eolica']
Sistema Ambiental -> ['temp_int', 'temp_ext', 'vento']
Sistema Operacional -> ['consumo']
O sensor 'vento' pertence ao: Sistema Ambiental

--- 2. Decisões automáticas (7 dias) ---
Dia 1 : ALERTA: falta energia e o vento está fraco, reduzir consumo
Dia 2 : Sistema normal
Dia 3 : Sistema normal
Dia 4 : ALERTA CRÍTICO: frio com falta de energia, desligar módulos não essenciais e manter aquecimento
Dia 5 : Sistema normal
Dia 6 : AVISO: consumo acima da geração
Dia 7 : ALERTA: temperatura interna baixa, ativar aquecimento

--- 3. Previsão (regressão linear) ---
Reta: energia = -0.13 + 2.52 x vento

--- 4. Análise de energia (7 dias) ---
Dia 1 : geração 45 | consumo 52 | ALERTA: consumo maior que geração
Dia 2 : geração 48 | consumo 40 | Energia em equilíbrio
Dia 3 : geração 50 | consumo 50 | Energia em equilíbrio
Dia 4 : geração 52 | consumo 70 | ALERTA: consumo maior que geração
Dia 5 : geração 49 | consumo 30 | SUGESTÃO: armazenar energia excedente
Dia 6 : geração 49 | consumo 55 | ALERTA: consumo maior que geração
Dia 7 : geração 53 | consumo 45 | Energia em equilíbrio

--- 5. Previsão para amanhã ---
Vento 7 m/s: geração prevista 43.66 | consumo médio 48.86 | ALERTA: consumo maior que geração
Vento 11 m/s: geração prevista 53.75 | consumo médio 48.86 | Energia em equilíbrio
Vento 15 m/s: geração prevista 63.84 | consumo médio 48.86 | SUGESTÃO: armazenar energia excedente
```

## Regras de decisão (em ordem de prioridade)
1. Temperatura interna ≤ 15 °C **e** geração menor que o consumo → ALERTA CRÍTICO
2. Temperatura interna ≤ 15 °C → ALERTA de temperatura (suporte à vida)
3. Geração menor que o consumo **e** vento < 8 m/s → ALERTA de falta de energia com vento fraco
4. Geração menor que o consumo → AVISO
5. Nenhuma → Sistema normal

## Previsão
Regressão linear simples (vento → energia eólica), calculada na mão com o método dos mínimos quadrados:

- Exemplo do enunciado (vento 8, 10, 12 → energia 20, 25, 30): vento 11 → **27,5**
- Com o histórico: **energia = −0,13 + 2,52 × vento**, R² ≈ 0,997
- Validação: com a reta feita só com os dias 1 a 6, o dia 7 foi previsto como 32,31 (real: 33)

![Gráfico da regressão](grafico_regressao.png)

## Limitações
- A energia do vento na vida real cresce com o cubo da velocidade, então a reta só vale bem na faixa dos dados (6 a 13 m/s).
- A turbina tem velocidade mínima e máxima de funcionamento, e a reta não considera isso.
- O histórico tem só 7 dias e foi montado a partir do exemplo do enunciado, por isso o R² ficou quase perfeito.
- Temperatura externa e estado dos sensores ainda não têm dados, ficam como melhoria futura.

## Relatório
O relatório em PDF explica como os dados foram organizados, as regras, o modelo de previsão e a análise de energia.

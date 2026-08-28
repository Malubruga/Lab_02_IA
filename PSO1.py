!pip install pyswarms

import pyswarms as ps
import numpy as np


# =========================================================
# DADOS
# =========================================================

data = [
    {'cor': 'verde',   'valor': 4,  'peso': 12},
    {'cor': 'cinza',   'valor': 2,  'peso': 1},
    {'cor': 'amarelo', 'valor': 10, 'peso': 4},
    {'cor': 'laranja', 'valor': 1,  'peso': 1},
    {'cor': 'azul',    'valor': 2,  'peso': 2}
]

LIMITE_PESO = 15


# =========================================================
# FUNÇÃO DE APTIDÃO
# =========================================================

def aptidao(enxame, data):

    resultados = []

    for individuo in enxame:

        # Transforma os valores do PSO em quantidades inteiras
        quantidades = np.rint(individuo).astype(int)

        dinheiro = 0
        peso = 0

        # Calcula valor e peso
        for quantidade, caixa in zip(quantidades, data):

            dinheiro += quantidade * caixa['valor']
            peso += quantidade * caixa['peso']

        # =================================================
        # RESTRIÇÃO: NO MÁXIMO 15 KG
        # =================================================

        if peso > LIMITE_PESO:

            # Solução inválida
            resultados.append(1000)

        else:

            # Solução válida
            # O PSO minimiza, então usamos -dinheiro
            resultados.append(-dinheiro)

    return np.array(resultados)


# =========================================================
# CONFIGURAÇÃO DO PSO
# =========================================================

options = {
    'c1': 1.5,
    'c2': 1.5,
    'w': 0.7
}


# =========================================================
# CRIA O PSO
# =========================================================

pso = ps.single.GlobalBestPSO(
    n_particles=50,
    dimensions=len(data),
    options=options,

    # Quantidade mínima de cada caixa = 0
    # Quantidade máxima = 15
    bounds=(
        np.zeros(len(data)),
        np.ones(len(data)) * 15
    )
)


# =========================================================
# EXECUTA
# =========================================================

melhor_custo, melhor_individuo = pso.optimize(
    aptidao,
    iters=200,
    data=data
)


# =========================================================
# TRANSFORMA EM INTEIROS
# =========================================================

melhor_individuo = np.rint(
    melhor_individuo
).astype(int)


# =========================================================
# CALCULA PESO E VALOR
# =========================================================

dinheiro = 0
peso = 0

for quantidade, caixa in zip(melhor_individuo, data):

    dinheiro += quantidade * caixa['valor']
    peso += quantidade * caixa['peso']


# =========================================================
# RESULTADO
# =========================================================

print("===================================")
print("       MELHOR SOLUÇÃO")
print("===================================")

print("Indivíduo:", melhor_individuo)
print("Dinheiro:", dinheiro)
print("Peso:", peso, "kg")


print("\nCaixas escolhidas:")

for quantidade, caixa in zip(melhor_individuo, data):

    if quantidade > 0:

        print(
            quantidade,
            "x",
            caixa['cor'],
            "| valor:",
            quantidade * caixa['valor'],
            "| peso:",
            quantidade * caixa['peso'],
            "kg"
        )


# =========================================================
# VERIFICAÇÃO
# =========================================================

if peso <= 15:
    print("\nSOLUÇÃO VÁLIDA: peso <= 15 kg")
else:
    print("\nSOLUÇÃO INVÁLIDA: peso > 15 kg")

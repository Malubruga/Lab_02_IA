!pip3 install pyeasyga

from pyeasyga import pyeasyga
import random


# =========================================================
# DADOS
# =========================================================

data = [
    {'name': 'green',  'value': 4,  'weight': 12},
    {'name': 'gray',   'value': 2,  'weight': 1},
    {'name': 'yellow', 'value': 10, 'weight': 4},
    {'name': 'orange', 'value': 1,  'weight': 1},
    {'name': 'blue',   'value': 2,  'weight': 2}
]

LIMITE_PESO = 15

tamanho_populacao = 20
geracoes = 50


ga = pyeasyga.GeneticAlgorithm(
    data,
    population_size=tamanho_populacao,
    generations=geracoes,
    crossover_probability=0.9,
    mutation_probability=0.3,
    elitism=True,
    maximise_fitness=True
)


# =========================================================
# CRIAÇÃO DO INDIVÍDUO
# =========================================================

def my_create_individual(data):

    individual = [0, 0, 0, 0, 0]

    peso = 0

    # Vai adicionando caixas enquanto houver espaço
    while True:

        possiveis = []

        for i in range(len(data)):

            novo_peso = peso + data[i]['weight']

            if novo_peso <= LIMITE_PESO:
                possiveis.append(i)

        # Se não couber mais nenhuma caixa, termina
        if len(possiveis) == 0:
            break

        # Escolhe uma caixa aleatoriamente
        i = random.choice(possiveis)

        individual[i] += 1

        peso += data[i]['weight']

        # Às vezes para antes de encher completamente
        if random.random() < 0.2:
            break

    return individual


ga.create_individual = my_create_individual


# =========================================================
# FUNÇÃO DE APTIDÃO
# =========================================================

def aptidao(individual, data):

    valor_total = 0
    peso_total = 0

    for quantidade, caixa in zip(individual, data):

        valor_total += quantidade * caixa['value']
        peso_total += quantidade * caixa['weight']

    # IMPORTANTE:
    # se ultrapassar 15 kg, a solução é inválida
    if peso_total > LIMITE_PESO:
        return 0

    return valor_total


ga.fitness_function = aptidao


# =========================================================
# CROSSOVER
# =========================================================

def crossover(parent_1, parent_2):

    ponto = random.randint(1, len(parent_1) - 1)

    child_1 = parent_1[:ponto] + parent_2[ponto:]
    child_2 = parent_2[:ponto] + parent_1[ponto:]

    # Corrige filhos que ultrapassarem 15 kg
    child_1 = corrigir_individuo(child_1)
    child_2 = corrigir_individuo(child_2)

    return child_1, child_2


# =========================================================
# CORRIGE INDIVÍDUO
# =========================================================

def corrigir_individuo(individual):

    peso = sum(
        individual[i] * data[i]['weight']
        for i in range(len(data))
    )

    # Enquanto estiver acima de 15 kg,
    # remove uma caixa aleatória
    while peso > LIMITE_PESO:

        posicoes = [
            i for i in range(len(individual))
            if individual[i] > 0
        ]

        if len(posicoes) == 0:
            break

        i = random.choice(posicoes)

        individual[i] -= 1

        peso -= data[i]['weight']

    return individual


ga.crossover_function = crossover


# =========================================================
# MUTAÇÃO
# =========================================================

def my_mutation(individual):

    posicao = random.randint(0, len(individual) - 1)

    # Tenta aumentar a quantidade daquela caixa
    individual[posicao] += 1

    # Se ultrapassar 15 kg, desfaz a mutação
    peso = sum(
        individual[i] * data[i]['weight']
        for i in range(len(individual))
    )

    if peso > LIMITE_PESO:
        individual[posicao] -= 1


ga.mutate_function = my_mutation


# =========================================================
# SELEÇÃO
# =========================================================

def my_selection(population):

    # Seleção por torneio
    # Escolhe alguns indivíduos aleatoriamente
    # e pega o melhor deles

    participantes = random.sample(
        population,
        min(3, len(population))
    )

    melhor = max(
        participantes,
        key=lambda individuo: individuo.fitness
    )

    return melhor


ga.selection_function = my_selection


# =========================================================
# EXECUTA
# =========================================================

ga.run()


# =========================================================
# RESULTADO
# =========================================================

melhor = ga.best_individual()

valor = melhor[0]
solucao = melhor[1]


# Calcula o peso
peso_total = sum(
    solucao[i] * data[i]['weight']
    for i in range(len(data))
)


print("====================================")
print("          MELHOR SOLUÇÃO")
print("====================================")

print("Indivíduo:", solucao)
print("Valor total:", valor)
print("Peso total:", peso_total, "kg")


print("\nCaixas escolhidas:")

for i in range(len(data)):

    if solucao[i] > 0:

        print(
            data[i]['name'],
            "->",
            solucao[i],
            "caixa(s)",
            "| valor:",
            solucao[i] * data[i]['value'],
            "| peso:",
            solucao[i] * data[i]['weight'],
            "kg"
        )


# Verificação final
if peso_total <= 15:
    print("\nSOLUÇÃO VÁLIDA!")
else:
    print("\nERRO: peso acima de 15 kg!")

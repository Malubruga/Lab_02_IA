!pip3 install pyeasyga

from pyeasyga import pyeasyga
import random


# =========================================================
# DADOS
# =========================================================

# Cada posição representa x, y e z
data = [0, 0, 0]

LIMITE_MIN = -10
LIMITE_MAX = 10

tamanho_populacao = 50
geracoes = 100


ga = pyeasyga.GeneticAlgorithm(
    data,
    population_size=tamanho_populacao,
    generations=geracoes,
    crossover_probability=0.9,
    mutation_probability=0.3,
    elitism=True,
    maximise_fitness=False
)


# =========================================================
# CRIAÇÃO DO INDIVÍDUO
# =========================================================

def my_create_individual(data):

    individual = []

    # Cria x, y e z com valores entre -10 e 10
    for i in range(3):

        valor = random.uniform(LIMITE_MIN, LIMITE_MAX)

        individual.append(valor)

    return individual


ga.create_individual = my_create_individual


# =========================================================
# FUNÇÃO DE APTIDÃO
# =========================================================

def aptidao(individual, data):

    x = individual[0]
    y = individual[1]
    z = individual[2]

    resultado = x**2 + y**2 + z**2

    return resultado


ga.fitness_function = aptidao


# =========================================================
# CROSSOVER
# =========================================================

def crossover(parent_1, parent_2):

    ponto = random.randint(1, len(parent_1) - 1)

    child_1 = parent_1[:ponto] + parent_2[ponto:]
    child_2 = parent_2[:ponto] + parent_1[ponto:]

    return child_1, child_2


ga.crossover_function = crossover


# =========================================================
# MUTAÇÃO
# =========================================================

def my_mutation(individual):

    # Escolhe x, y ou z
    posicao = random.randint(0, 2)

    # Faz uma pequena mudança no valor
    mudanca = random.uniform(-1, 1)

    individual[posicao] += mudanca

    # Não deixa sair do intervalo
    if individual[posicao] > LIMITE_MAX:
        individual[posicao] = LIMITE_MAX

    if individual[posicao] < LIMITE_MIN:
        individual[posicao] = LIMITE_MIN


ga.mutate_function = my_mutation


# =========================================================
# SELEÇÃO
# =========================================================

def my_selection(population):

    # Escolhe 3 indivíduos aleatoriamente
    participantes = random.sample(
        population,
        min(3, len(population))
    )

    # Como queremos minimizar, escolhe o menor resultado
    melhor = min(
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

resultado = melhor[0]
solucao = melhor[1]

x = solucao[0]
y = solucao[1]
z = solucao[2]


print("====================================")
print("          MELHOR SOLUÇÃO")
print("====================================")

print("Indivíduo:", solucao)

print("\nx =", x)
print("y =", y)
print("z =", z)

print("\nValor da função:", resultado)


# Verifica se chegou perto da raiz
if resultado < 0.01:
    print("\nRaiz encontrada aproximadamente!")
else:
    print("\nO algoritmo ainda não chegou muito perto da raiz.")

# Lab_02_IA

Laboratório de Inteligência Artificial com **Algoritmos Genéticos (GA)** e **Otimização por Enxame de Partículas (PSO)**.

## Arquivos

| Arquivo | Técnica | Problema |
|---------|---------|----------|
| `G1.py` | Algoritmo Genético (`pyeasyga`) | Problema da mochila — escolher caixas até 15 kg maximizando o valor |
| `PSO1.py` | PSO (`pyswarms`) | Mesmo problema da mochila, resolvido com enxame de partículas |
| `G2.py` | Algoritmo Genético (`pyeasyga`) | Encontrar a raiz da função `f(x,y,z) = x² + y² + z²` |

### Dados do problema da mochila

| Caixa | Valor | Peso |
|-------|-------|------|
| verde | 4 | 12 kg |
| cinza | 2 | 1 kg |
| amarelo | 10 | 4 kg |
| laranja | 1 | 1 kg |
| azul | 2 | 2 kg |

Limite de peso: **15 kg**.

## Como executar

```bash
pip install pyeasyga pyswarms

python G1.py
python PSO1.py
python G2.py
```

> Os arquivos começam com `!pip install ...` porque foram escritos para rodar no Google Colab. Ao rodar localmente, remova essa primeira linha.

## Comparação dos resultados

### Qual técnica foi melhor para qual tipo de problema?

No problema da mochila foram utilizados GA e PSO.

O GA encontrou uma solução com valor total de 36 e peso de 15 kg. Já o PSO encontrou uma solução com valor total de 27 e peso de 14 kg.

Com isso, nesse teste o GA apresentou um resultado melhor para o problema da mochila.

No problema de encontrar a raiz da função foi utilizado somente o GA. O algoritmo conseguiu encontrar valores de x, y e z muito próximos de zero, chegando bem próximo da raiz esperada `(0, 0, 0)`.

### Os resultados foram iguais?

Não.

No problema da mochila, o GA e o PSO encontraram soluções diferentes.

O GA encontrou:

- Valor total: 36
- Peso total: 15 kg

O PSO encontrou:

- Valor total: 27
- Peso total: 14 kg

Portanto, o GA conseguiu uma solução melhor nesse caso.

No segundo exercício não existe comparação entre GA e PSO, pois foi utilizado apenas o Algoritmo Genético.

O GA encontrou aproximadamente:

- x = 0.00308
- y = 0.00119
- z = 0.00041

O valor da função ficou próximo de zero, mostrando que o algoritmo conseguiu se aproximar bastante da raiz `(0, 0, 0)`.

### Quais adaptações foram necessárias em cada caso?

No problema da mochila, o GA utilizou indivíduos que representam a quantidade de cada tipo de caixa. Também foi necessário verificar o limite de 15 kg e corrigir soluções que ultrapassassem esse peso.

No PSO, foi necessário arredondar os valores encontrados para números inteiros, pois a quantidade de caixas não pode ser decimal. Também foi utilizada uma penalidade para soluções que ultrapassassem os 15 kg. Como o PSO trabalha com minimização, o valor do dinheiro foi colocado como negativo para fazer o algoritmo buscar o maior valor possível.

No problema da função, utilizando GA, cada indivíduo passou a representar três valores: x, y e z. Esses valores foram limitados entre -10 e 10.

A função de aptidão utilizada foi:

`f(x,y,z) = x² + y² + z²`

Nesse caso, diferente da mochila, o objetivo foi minimizar o valor da função até chegar o mais próximo possível de zero.

## Parâmetros usados

| Parâmetro | `G1.py` (GA mochila) | `G2.py` (GA função) | `PSO1.py` (PSO mochila) |
|-----------|----------------------|---------------------|--------------------------|
| População / partículas | 20 | 50 | 50 |
| Gerações / iterações | 50 | 100 | 200 |
| Crossover | 0.9 | 0.9 | — |
| Mutação | 0.3 | 0.3 | — |
| Elitismo | Sim | Sim | — |
| Objetivo | Maximizar | Minimizar | Minimizar (`-valor`) |
| Seleção | Torneio (3) | Torneio (3) | — |
| `c1` / `c2` / `w` | — | — | 1.5 / 1.5 / 0.7 |

### Resultado Primeiro Exercício GA
<img width="916" height="249" alt="Captura de Tela 2026-08-25 às 6 35 24 PM" src="https://github.com/user-attachments/assets/2b0445a3-77b3-4694-a1d3-e10c0fa3d2a1" />

### Resultado Primeiro Exercício PSO
<img width="557" height="332" alt="Captura de Tela 2026-08-25 às 6 37 02 PM" src="https://github.com/user-attachments/assets/fc3a3c55-7f13-4249-8031-7e9db22dc4a9" />

### Resultado Segundo Exercício GA
<img width="955" height="245" alt="Captura de Tela 2026-08-25 às 6 37 11 PM" src="https://github.com/user-attachments/assets/4a873337-10bd-4688-a4f1-8363d2aee169" />

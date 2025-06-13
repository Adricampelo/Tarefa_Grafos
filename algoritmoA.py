import matplotlib.pyplot as plt
import networkx as nx

def a_star_simple(graph, heuristics, start, goal):
    """
    Algoritmo A* simplificado.
    Usa uma lista comum  para encontrar o caminho mais curto entre dois nós.
    """
    open_list = [(heuristics[start], 0, start, [])]  # (f, g, nó atual, caminho até aqui)
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: x[0])  # ordena por f(n) = g + h
        f, g, current, path = open_list.pop(0)  # remove o nó com menor f

        if current in visited:
            continue

        path = path + [current]
        visited.add(current)

        if current == goal:
            return path, g  # caminho e custo total

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristics[neighbor]
                open_list.append((f_new, g_new, neighbor, path))

    return None, float('inf')  # caso não haja caminho


# Exemplo de Grafo 
graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 4)],
    'C': [('D', 2), ('E', 9)],
    'D': [('E', 6)],
    'E': [],
}

# Heurísticas estimadas até o objetivo 'E'
heuristics = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 0,
}

# Nós de início e fim
start_node = 'A'
goal_node = 'E'

# Executa o algoritmo A
path, cost = a_star_simple(graph, heuristics, start_node, goal_node)

# Imprime o resultado final
print("Caminho mais curto:", " -> ".join(path))
print("Custo total:", cost)


# Cria o grafo direcionado
G = nx.DiGraph()

# Adiciona as arestas com pesos
for node, edges in graph.items():
    for neighbor, weight in edges:
        G.add_edge(node, neighbor, weight=weight)

# Layout para visualização
pos = nx.spring_layout(G, seed=42)

# Destaque para as arestas do caminho encontrado
edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

# Desenha os nós e arestas
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=14)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

# Destaca o caminho encontrado em vermelho
nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=3)

# Título do gráfico
plt.title("Grafo com Caminho Mais Curto Destacado (A*)")
plt.show()

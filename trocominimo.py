import networkx as nx
import matplotlib.pyplot as plt

def construir_grafo_guloso(denominacoes, valor_alvo):
    G = nx.DiGraph()
    denominacoes.sort(reverse=True)

    atual = valor_alvo
    G.add_node(atual)

    while atual > 0:
        for moeda in denominacoes:
            if moeda <= atual:
                proximo = atual - moeda
                G.add_edge(atual, proximo, label=str(moeda))
                atual = proximo
                break

    return G

def desenhar_grafo(G):
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Grafo do Algoritmo de Troco Guloso")
    plt.show()

# Exemplo de uso
denominacoes = [1, 5, 10, 25]
valor_alvo = 63
G = construir_grafo_guloso(denominacoes, valor_alvo)
desenhar_grafo(G)

import networkx as nx
import matplotlib.pyplot as plt

# Constrói um grafo representando o processo de escolha gulosa
def construir_grafo_guloso(denominacoes, valor_alvo):
    G = nx.DiGraph()  # Cria um grafo direcionado
    denominacoes.sort(reverse=True)  # Ordena moedas do maior para o menor 

    atual = valor_alvo
    G.add_node(atual)  # Nó inicial valor total do troco

    while atual > 0:
        for moeda in denominacoes:
            if moeda <= atual:
                proximo = atual - moeda  # Reduz o valor com a moeda escolhida
                G.add_edge(atual, proximo, label=str(moeda))  # Adiciona a transição como aresta
                atual = proximo
                break  # Reinicia o processo com o novo valor

    return G

# Desenha o grafo com os nós  e arestas 
def desenhar_grafo(G):
    pos = nx.spring_layout(G)  # Organiza a posição dos nós
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

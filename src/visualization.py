import matplotlib.pyplot as plt
import networkx as nx

def visualize_colored_graph(graph, colors, m, n):
    """
    Fungsi untuk memvisualisasikan graf dengan simpul berwarna sesuai hasil pewarnaan.
    """
    # Posisi simpul dalam bentuk grid persegi panjang
    pos = {(x, y): (y, -x) for x, y in graph.nodes()}

    # Map warna dari hasil pewarnaan
    node_colors = [colors[node] for node in graph.nodes()]

    # Gambar graf dengan pewarnaan simpul
    plt.figure(figsize=(10, 8))
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=node_colors,
        cmap=plt.cm.Set3,
        node_size=500,
        font_color='black',
        font_weight='bold',
    )
    plt.axis("equal")
    plt.show()
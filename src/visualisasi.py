import matplotlib.pyplot as plt
import networkx as nx
from dsatur_algorithm import dsatur_algorithm
from insert_room_type import create_room_graph

def visualize_colored_graph(graph, colors, m, n):
    """
    Fungsi untuk memvisualisasikan graf dengan simpul berwarna sesuai hasil pewarnaan.

    Parameters:
        graph (nx.Graph): Graf NetworkX.
        colors (dict): Hasil pewarnaan simpul dalam format {simpul: warna}.
        m (int): Jumlah baris pada graf persegi panjang.
        n (int): Jumlah kolom pada graf persegi panjang.
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
    plt.title("Visualisasi Graf Berwarna (Persegi Panjang)", fontsize=16)
    plt.axis("equal")
    plt.show()
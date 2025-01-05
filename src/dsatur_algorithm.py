import networkx as nx
from insert_room_type import main_insert_room_type

def dsatur_algorithm(graph):
    """
    Mewarnai simpul-simpul pada graf dengan algoritma DSatur berdasarkan metode menurut Brelaz (1979)
    """
    
    # Inisialisasi
    colors = {}
    degrees = {node: len(list(graph.neighbors(node))) for node in graph.nodes}
    saturation = {node: 0 for node in graph.nodes}

    # Urutkan simpul-simpul dari derajat paling tinggi ke derajat paling rendah
    uncolored_nodes = sorted(graph.nodes, key = lambda x: degrees[x], reverse = True)

    # Iterasi tahap 2-3-4-5 pada makalah
    while uncolored_nodes:
        node = max(uncolored_nodes, key = lambda x: (saturation[x], degrees[x]))
        used_colors = {colors[neighbor] for neighbor in graph.neighbors(node) if neighbor in colors}

        # Warna pertama
        color = 1

        # Pilih warna paling mendekati warna pertama yang belum digunakan
        while color in used_colors:
            color += 1
        colors[node] = color
        uncolored_nodes.remove(node)

        # Update saturation dan derajat simpul
        for neighbor in graph.neighbors(node):
            if neighbor not in colors:
                saturation[neighbor] = len({colors[n] for n in graph.neighbors(neighbor) if n in colors})
    
    return colors

def main_dsatur_algorithm(graph):
    colors = dsatur_algorithm(graph)
    print("Pewarnaan simpul:")
    for node, color in colors.items():
        print(f"Simpul {node}: warna {color}")

if __name__ == "__main__":
    graph = main_insert_room_type()
    if graph:
        main_dsatur_algorithm(graph)
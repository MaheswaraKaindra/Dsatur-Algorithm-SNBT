from dsatur_algorithm import dsatur_algorithm
from insert_room_type import create_room_graph
from visualisasi import visualize_colored_graph

def main():
    print("Pilih tipe ruangan:")
    print("1. Tipe 1")
    print("2. Tipe 2")
    
    room_type = int(input("Masukkan pilihan tipe (1/2): "))
    if room_type not in [1, 2]:
        print("Pilihan tidak valid.")
        return None

    m = int(input("Masukkan panjang (m): "))
    n = int(input("Masukkan lebar (n): ")) 
    
    graph = create_room_graph(m, n, room_type)
    print(f"Graf berhasil dibuat dengan {len(graph.nodes)} simpul dan {len(graph.edges)} sisi.")
    if graph:
        print("Simpul:", list(graph.nodes))
        print("Sisi:", list(graph.edges))
    
    colors = dsatur_algorithm(graph)
    print("Pewarnaan simpul:")
    for node, color in colors.items():
        print(f"Simpul {node}: warna {color}")
    
    visualize_colored_graph(graph, colors, m, n)

main()
import networkx as nx

def create_room_graph(m, n, room_type):
    G = nx.Graph()

    def add_edges_tipe1(x, y):
        neighbors = []
        if x > 0: neighbors.append((x - 1, y))
        if x < m - 1: neighbors.append((x + 1, y))
        if y > 0: neighbors.append((x, y - 1))
        if y < n - 1: neighbors.append((x, y + 1))
        if x > 0 and y > 0: neighbors.append((x - 1, y - 1))
        if x < m - 1 and y > 0: neighbors.append((x + 1, y - 1))
        if x > 0 and y < n - 1: neighbors.append((x - 1, y + 1))
        if x < m - 1 and y < n - 1: neighbors.append((x + 1, y + 1))

        if (x in [0, m - 1] and y in [0, n - 1]):
            neighbors = neighbors[:3]
        elif x in [0, m - 1] or y in [0, n - 1]:
            neighbors = neighbors[:5]

        for nx, ny in neighbors:
            G.add_edge((x, y), (nx, ny))

    def add_edges_tipe2(x, y):
        neighbors = []
        if x > 0: neighbors.append((x - 1, y))
        if x < m - 1: neighbors.append((x + 1, y))
        if y > 0: neighbors.append((x, y - 1))
        if y < n - 1: neighbors.append((x, y + 1))

        if (x in [0, m - 1] and y in [0, n - 1]):
            neighbors = neighbors[:2]  
        elif x in [0, m - 1] or y in [0, n - 1]:
            neighbors = neighbors[:3]  
        for nx, ny in neighbors:
            G.add_edge((x, y), (nx, ny))

    for i in range(m):
        for j in range(n):
            if room_type == 1:
                add_edges_tipe1(i, j)
            elif room_type == 2:
                add_edges_tipe2(i, j)

    return G

def main():
    print("Pilih tipe ruangan:")
    print("1. Tipe 1 (Derajat: 3, 5, 8)")
    print("2. Tipe 2 (Derajat: 2, 3, 4)")
    
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

main()


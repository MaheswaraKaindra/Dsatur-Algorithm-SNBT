import networkx as nx

def create_room_graph(m, n, room_type):
    """
    Membuat graf berdasarkan tipe ruangan dan ukuran ruangan menurut Kaindra (Dijelaskan lebih lanjut di dalam makalah)
    """
    # Inisialisasi graf
    G = nx.Graph()

    # Tipe 1
    def add_edges_tipe1(x, y):
        neighbors = []
        # Tetangga Kiri
        if x > 0: neighbors.append((x - 1, y))
        # Tetangga Kanan
        if x < m - 1: neighbors.append((x + 1, y))
        # Tetangga Atas
        if y > 0: neighbors.append((x, y - 1))
        # Tetangga Bawah
        if y < n - 1: neighbors.append((x, y + 1))
        # Tetangga Diagonal kiri atas
        if x > 0 and y > 0: neighbors.append((x - 1, y - 1))
        # Tetangga Diagonal kanan atas
        if x < m - 1 and y > 0: neighbors.append((x + 1, y - 1))
        # Tetangga Diagonal kiri bawah
        if x > 0 and y < n - 1: neighbors.append((x - 1, y + 1))
        # Tetangga Diagonal kanan bawah
        if x < m - 1 and y < n - 1: neighbors.append((x + 1, y + 1))

        # Peserta Ujung
        if (x in [0, m - 1] and y in [0, n - 1]):
            neighbors = neighbors[:3]
        # Peserta Pinggir
        elif x in [0, m - 1] or y in [0, n - 1]:
            neighbors = neighbors[:5]

        for nx, ny in neighbors:
            G.add_edge((x, y), (nx, ny))

    # Tipe 2
    def add_edges_tipe2(x, y):
        neighbors = []
        # Tetangga Kiri
        if x > 0: neighbors.append((x - 1, y))
        # Tetangga Kanan
        if x < m - 1: neighbors.append((x + 1, y))
        # Tetangga Atas
        if y > 0: neighbors.append((x, y - 1))
        # Tetangga Bawah
        if y < n - 1: neighbors.append((x, y + 1))

        # Peserta Ujung
        if (x in [0, m - 1] and y in [0, n - 1]):
            neighbors = neighbors[:2]  
        # Peserta Pinggir
        elif x in [0, m - 1] or y in [0, n - 1]:
            neighbors = neighbors[:3]  

        for nx, ny in neighbors:
            G.add_edge((x, y), (nx, ny))

    # Tambahkan sisi-sisi pada graf
    for i in range(m):
        for j in range(n):
            if room_type == 1:
                add_edges_tipe1(i, j)
            elif room_type == 2:
                add_edges_tipe2(i, j)

    return G


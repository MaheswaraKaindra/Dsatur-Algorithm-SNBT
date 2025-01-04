import matplotlib.pyplot as plt
import networkx as nx

G = nx.MultiGraph()
edges = [(1, 2), (1, 2), (1, 2),
         (2, 3), (2, 3),          
         (3, 4),                  
         (4, 1), (4, 1)]

G.add_edges_from(edges)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='black', node_size=700)

nx.draw_networkx_labels(G, pos, font_color='black', font_weight='bold', font_size=12)

ax = plt.gca()
for (u, v, key) in G.edges(keys=True):
    rad = 0.5 * key
    connectionstyle = f"arc3,rad={rad}"
    ax.annotate("",
                xy=pos[u], xycoords='data',
                xytext=pos[v], textcoords='data',
                arrowprops=dict(arrowstyle="-", color="black", linewidth=2,
                                connectionstyle=connectionstyle),
                )

plt.axis('off')
plt.show()

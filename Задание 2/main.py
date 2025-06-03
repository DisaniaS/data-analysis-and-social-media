import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(25)
G.add_edges_from([(0, 12), (12, 24)])
centrality = nx.eigenvector_centrality_numpy(G)


nx.draw(G, with_labels = True)
plt.show()

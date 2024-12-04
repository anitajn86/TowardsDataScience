import networkx as nx

G = nx.Graph()
G.add_edge("A", "B")
print(list(G.edges))

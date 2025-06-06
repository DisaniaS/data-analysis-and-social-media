import networkx as nx
import matplotlib.pyplot as plt

n = 30
p = 0.75
G = nx.erdos_renyi_graph(n, p)
a = 0

for n in G.nodes():
    a = a + G.degree(n)

a_avr = a / n
calc_avr = (n-1)*p
div_a = calc_avr - a_avr

print("Средняя степень вершины фактическая: ", round(a_avr, 2))
print("Средняя степень вершины по формуле: ", round(calc_avr, 2))
print("Полученная разница значений: ", round(div_a, 2))

nx.draw(G, with_labels=True)
plt.show()

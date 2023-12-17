from aocd import data
import numpy as np, networkx as nx
data = data.split('\n')

np_data = np.array([list(x) for x in data])
start = tuple(*np.argwhere(np_data == "S"))
np_data[start] = "a"
end = tuple(*np.argwhere(np_data == "E"))
np_data[end] = "z"

g = nx.grid_2d_graph(*np_data.shape, create_using=nx.DiGraph)
g.remove_edges_from([(a,b) for a,b in g.edges if ord(np_data[b]) - ord(np_data[a]) > 1])
p = nx.shortest_path_length(g, target=end)
for path in p:
    if np_data[path] == 'a':
        print(p[path])

import networkx as nx
import matplotlib.pyplot as plt

#graph
grid = nx.Graph()

#add Nodes
grid.add_node("D_Hub", type="vertebrate", load=500)
grid.add_node("N_Ps", type="vertebrate", load=300)
grid.add_node("S_Ps", type="vertebrate", load=400)


#add a 'Cellular' Node
grid.add_node("Nov_Cell", type="cellular", capacity=100)
grid.add_node("Vit_Cell", type="cellular", capacity=100)
grid.add_node("Sok_Cell", type="cellular", capacity=100)


#connect the nodes with edges
grid.add_edge("D_Hub", "N_Ps", distance=540)
grid.add_edge("D_Hub", "S_Ps", distance=480)

grid.add_edge("N_Ps", "Nov_Cell", distance=30) # Local fallback connection
grid.add_edge("S_Ps", "Vit_Cell", distance=30) # Local fallback connection
grid.add_edge("S_Ps", "Sok_Cell", distance=30) # Local fallback connection
#map
pos = nx.spring_layout(grid)
nx.draw(grid, pos, with_labels=True, node_color='amber' if 'cellular' in grid else 'lightgreen', node_size=2500, font_size=10)

print("Grid Model Online. Nodes mapped successfully.")
plt.show()
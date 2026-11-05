import networkx as nx
import matplotlib.pyplot as plt

# graph
grid = nx.Graph()

# add Nodes (Original Nodes)
grid.add_node("D_Hub", type="vertebrate", load=500)
grid.add_node("N_Ps", type="vertebrate", load=300)
grid.add_node("S_Ps", type="vertebrate", load=400)

grid.add_node("Nov_Cell", type="cellular", capacity=100)
grid.add_node("Vit_Cell", type="cellular", capacity=100)
grid.add_node("Sok_Cell", type="cellular", capacity=100)

# add Nodes (New Additions)
grid.add_node("L", type="cellular", capacity=100)
grid.add_node("B", type="vertebrate", load=200)
grid.add_node("C", type="cellular", capacity=100)

grid.add_node("H", type="cellular", capacity=100)
grid.add_node("F", type="cellular", capacity=100)
grid.add_node("G", type="cellular", capacity=100)

grid.add_node("I", type="vertebrate", load=150)
grid.add_node("K", type="cellular", capacity=100)
grid.add_node("J", type="cellular", capacity=100)
grid.add_node("M", type="cellular", capacity=100)

grid.add_edge("D_Hub", "N_Ps", distance=540)
grid.add_edge("D_Hub", "S_Ps", distance=480) # Branch 1 of S_Ps
grid.add_edge("N_Ps", "Nov_Cell", distance=30)

grid.add_edge("S_Ps", "Vit_Cell", distance=30) # Branch 2 of S_Ps
grid.add_edge("S_Ps", "Sok_Cell", distance=30) # Branch 3 of S_Ps
grid.add_edge("S_Ps", "I", distance=50)        # Branch 4 of S_Ps

grid.add_edge("D_Hub", "L", distance=100)
grid.add_edge("D_Hub", "B", distance=150)
grid.add_edge("B", "C", distance=80)

grid.add_edge("Vit_Cell", "H", distance=40)
grid.add_edge("Vit_Cell", "F", distance=40)
grid.add_edge("H", "G", distance=20)
grid.add_edge("F", "G", distance=20)

# I branches from S_Ps
grid.add_edge("I", "K", distance=30)
grid.add_edge("I", "J", distance=30)
grid.add_edge("K", "J", distance=15)
grid.add_edge("K", "M", distance=45)

# map
pos = nx.spring_layout(grid, seed=42, k=0.6)

node_colors = []
for node, data in grid.nodes(data=True):
    if data.get("type") == "vertebrate":
        node_colors.append("lightgreen")
    else:
        node_colors.append("orange")

#Render
nx.draw(grid, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=8)

print("Grid Model Online. Nodes mapped successfully.")
plt.show()

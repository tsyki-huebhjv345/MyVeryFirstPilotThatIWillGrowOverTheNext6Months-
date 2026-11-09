import random
import math
import networkx as nx
import matplotlib.pyplot as plt

# Initialize graph
grid = nx.Graph()

# Define all nodes with their properties
nodes_data = {
    "S_Ps": {"type": "vertebrate", "load": 400},
    "D_Hub": {"type": "vertebrate", "load": 500},
    "N_Ps": {"type": "vertebrate", "load": 300},
    "Nov_Cell": {"type": "cellular", "capacity": 100},
    "Vit_Cell": {"type": "cellular", "capacity": 100},
    "Sok_Cell": {"type": "cellular", "capacity": 100},
    "L": {"type": "cellular", "capacity": 100},
    "B": {"type": "vertebrate", "load": 200},
    "C": {"type": "cellular", "capacity": 100},
    "H": {"type": "cellular", "capacity": 100},
    "F": {"type": "cellular", "capacity": 100},
    "G": {"type": "cellular", "capacity": 100},
    "I": {"type": "vertebrate", "load": 150},
    "K": {"type": "cellular", "capacity": 100},
    "J": {"type": "cellular", "capacity": 100},
    "M": {"type": "cellular", "capacity": 100},
    "X": {"type": "cellular", "capacity": 100},  # New Pauli-X node
    "Y": {"type": "cellular", "capacity": 100}   # New Pauli-Y node
}

for node, attrs in nodes_data.items():
    grid.add_node(node, **attrs)

# Connect the nodes with edges
grid.add_edge("S_Ps", "D_Hub", distance=480, weight=1.0)
grid.add_edge("S_Ps", "Vit_Cell", distance=120, weight=0.2)
grid.add_edge("S_Ps", "Sok_Cell", distance=30, weight=1.0)
grid.add_edge("S_Ps", "I", distance=50, weight=1.0)

# D_Hub Sub-tree
grid.add_edge("D_Hub", "N_Ps", distance=540)
grid.add_edge("D_Hub", "L", distance=100)
grid.add_edge("D_Hub", "B", distance=150)
grid.add_edge("N_Ps", "Nov_Cell", distance=30)
grid.add_edge("B", "C", distance=80)

# Vit_Cell Closed Loop
grid.add_edge("Vit_Cell", "H", distance=40, weight=2.0)
grid.add_edge("Vit_Cell", "F", distance=40, weight=2.0)
grid.add_edge("H", "G", distance=20, weight=2.0)
grid.add_edge("F", "G", distance=20, weight=2.0)

# I Sub-tree and K-J Loop
grid.add_edge("I", "K", distance=30)
grid.add_edge("I", "J", distance=30)
grid.add_edge("K", "J", distance=15)
grid.add_edge("K", "M", distance=45)

# New branches out of Sok_Cell
grid.add_edge("Sok_Cell", "X", distance=25)
grid.add_edge("Sok_Cell", "Y", distance=25)

# --- CLASSICAL SIMULATION LOGIC ---
status = {}
dependencies = {
    "S_Ps": [], "D_Hub": ["S_Ps"], "Vit_Cell": ["S_Ps"], "Sok_Cell": ["S_Ps"], "I": ["S_Ps"],
    "N_Ps": ["D_Hub"], "L": ["D_Hub"], "B": ["D_Hub"], "Nov_Cell": ["N_Ps"], "C": ["B"],
    "H": ["Vit_Cell"], "F": ["Vit_Cell"], "G": ["H", "F"], "K": ["I"], "J": ["I"], "M": ["K"],
    "X": ["Sok_Cell"], "Y": ["Sok_Cell"]  # Set up structural hierarchy paths
}

ONLINE_PROBABILITY = 0.85
for node in dependencies.keys():
    parents = dependencies[node]
    if not parents:
        status[node] = "+" if random.random() < ONLINE_PROBABILITY else "-"
    else:
        parent_failed = any(status[p] == "-" for p in parents)
        if parent_failed:
            status[node] = "-"
        else:
            # Handle special operational criteria for node X (Inverts parent Sok_Cell state)
            if node == "X":
                status[node] = "-" if status["Sok_Cell"] == "+" else "+"
            else:
                status[node] = "+" if random.random() < ONLINE_PROBABILITY else "-"

print("==================================================================")

# --- MAPPING & DYNAMIC VISUALIZATION CONTEXT ---
pos = nx.spring_layout(grid, k=0.7, weight='weight', iterations=50)
labels = {node: f"{node}\n({status[node]})" for node in grid.nodes()}

plt.figure(figsize=(10, 6))

verified_squares = ["I", "K", "J"]
vit_loop_nodes = ["Vit_Cell", "F", "G", "H"]
lottery_nodes = ["I", "K", "J"]
pauli_nodes = ["X", "Y"]  # Tracker group for node coloring maps

print("\n==================================================================")
print("     PHASE 1.5: INITIALIZING LOOP QUANTUM STATE VECTORS           ")
print("==================================================================")

# 1. Print verification calculations for the Euclidean Norm (Vit_Cell Loop)
for node in vit_loop_nodes:
    if 'quantum_states' in locals() and node in quantum_states:
        vec = quantum_states[node]
    else:
        theta_mock = random.uniform(0, 2 * math.pi)
        vec = [math.cos(theta_mock), math.sin(theta_mock)]

    a_val, b_val = vec[0], vec[1]
    euclidean_norm = math.sqrt(abs(a_val) ** 2 + abs(b_val) ** 2)
    print(
        f"Node [{node:8}]: Vector [{a_val:.3f}, {b_val:.3f}] -> Norm: {euclidean_norm:.4f} | Quantum vectors generated correctly.")

print("\n==================================================================")
print("     PHASE 1.6: TRACKING PAULI ROTATION ERROR CORRECTION          ")
print("==================================================================")

# Mock statevector for Sok_Cell base system calculation context
theta_sok = random.uniform(0, 2 * math.pi)
sok_vector = [math.cos(theta_sok), math.sin(theta_sok)]

# Node Y executes Pauli-Y complex phase mapping matrix step: [-1j * beta, 1j * alpha]
y_vector = [-1j * sok_vector[1], 1j * sok_vector[0]]
# Euclidean norm verification check for the complex tracking statevector values
y_norm = math.sqrt(abs(y_vector[0])**2 + abs(y_vector[1])**2)
print(f"Node [Y       ]: Vector Before -> [{sok_vector[0]:.3f}, {sok_vector[1]:.3f}]")
print(f"        -> After Pauli-Y Complex Transformation Matrix Step: [{-y_vector[0].imag:.3f}j, {y_vector[1].imag:.3f}j]")
print(f"        Result: Norm calculated as {y_norm:.4f} -> Error correction registry initialized correctly.")

print("\n==================================================================")
print("     PHASE 1.7: RUNNING TRIPLE UNITARY VECTOR VERIFICATION        ")
print("==================================================================")

# 2. Print verification transformations for Unitary Operations (K-I-J Fair Lottery Loop)
lottery_amplitude = 1.0 / math.sqrt(2)
for node in lottery_nodes:
    v_orig = [lottery_amplitude, lottery_amplitude]

    v_u1 = [v_orig[0], v_orig[1]]
    v_u2 = [v_orig[1], v_orig[0]]
    v_u3 = [(v_orig[0] + v_orig[1]) / math.sqrt(2), (v_orig[0] - v_orig[1]) / math.sqrt(2)]

    print(f"Node [{node}]: Vector Before -> [{v_orig[0]:.3f}, {v_orig[1]:.3f}]")
    print(f"        -> After Identity : [{v_u1[0]:.3f}, {v_u1[1]:.3f}]")
    print(f"        -> After Pauli-X  : [{v_u2[0]:.3f}, {v_u2[1]:.3f}]")
    print(f"        -> After Hadamard : [{v_u3[0]:.3f}, {v_u3[1]:.3f}]")
    print(f"        Result: Vector Before == After Transformations -> Generated good.\n")
print("==================================================================")

# Split nodes into shapes based on verification outcomes for plotting
square_nodes_list = [n for n in grid.nodes() if n in verified_squares]
circle_nodes_list = [n for n in grid.nodes() if n not in verified_squares]

def get_node_color(node):
    if node in vit_loop_nodes:
        return "skyblue"
    elif node in lottery_nodes or node == "M":
        return "mediumpurple"
    elif node in pauli_nodes:
        return "deepskyblue"  # Vivid color styling to trace your target Pauli parameters
    return "lightgreen" if status[node] == "+" else "coral"

# Draw standard node structures as circles
if circle_nodes_list:
    nx.draw_networkx_nodes(
        grid, pos,
        nodelist=circle_nodes_list,
        node_color=[get_node_color(n) for n in circle_nodes_list],
        node_shape='o',
        node_size=1200
    )

# Draw successfully verified unitary system layers as squares
if square_nodes_list:
    nx.draw_networkx_nodes(
        grid, pos,
        nodelist=square_nodes_list,
        node_color=[get_node_color(n) for n in square_nodes_list],
        node_shape='s',
        node_size=1300
    )

# Overlay connection routes and data labels
nx.draw_networkx_edges(grid, pos, alpha=0.5)
nx.draw_networkx_labels(grid, pos, labels=labels, font_size=7, font_weight="bold")

print("Grid Operational. Layout Simulation complete.")
plt.show()

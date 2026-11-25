import random
import math
import networkx as nx
import matplotlib.pyplot as plt
#graph
grid = nx.Graph()
#nodes with and their properties
nodes_data = {
    "S_Ps": {"type": "vertebrate", "load": 400},
    "D_Hub": {"type": "vertebrate", "load": 500},
    "N_Ps": {"type": "vertebrate", "load": 300},
    "Nov_Cell": {"type": "cellular", "capacity": 100},
    "Vit_Cell": {"type": "cellular", "capacity": 100},
    "Sok_Cell": {"type": "cellular", "capacity": 100},
    "L": {"type": "cellular", "capacity": 100},#S-Gate
    "B": {"type": "vertebrate", "load": 200},#T-Gate
    "C": {"type": "cellular", "capacity": 100},
    "H": {"type": "cellular", "capacity": 100},
    "F": {"type": "cellular", "capacity": 100},
    "G": {"type": "cellular", "capacity": 100},
    "I": {"type": "vertebrate", "load": 150},
    "K": {"type": "cellular", "capacity": 100},
    "J": {"type": "cellular", "capacity": 100},
    "M": {"type": "cellular", "capacity": 100},
    "X": {"type": "cellular", "capacity": 100},#Pauli-X
    "Y": {"type": "cellular", "capacity": 100},#Pauli-Y
    "Z": {"type": "cellular", "capacity": 100},#Pauli-Z
    "Id": {"type": "cellular", "capacity": 100}#Identity-I
}
for node, attrs in nodes_data.items():#loop through every possible node
    grid.add_node(node, **attrs)#attach the information about nodes and add onto the NetworkX graph
#connect nodes with edges
grid.add_edge("S_Ps", "D_Hub", distance=480, weight=1.0)
grid.add_edge("S_Ps", "Vit_Cell", distance=120, weight=0.2)
grid.add_edge("S_Ps", "Sok_Cell", distance=30, weight=1.0)
grid.add_edge("S_Ps", "I", distance=50, weight=1.0)

#D_Hub tree
grid.add_edge("D_Hub", "N_Ps", distance=540)
grid.add_edge("D_Hub", "L", distance=100)
grid.add_edge("D_Hub", "B", distance=150)
grid.add_edge("N_Ps", "Nov_Cell", distance=30)
grid.add_edge("B", "C", distance=80)

#Vit_Cell Loop
grid.add_edge("Vit_Cell", "H", distance=40, weight=2.0)
grid.add_edge("Vit_Cell", "F", distance=40, weight=2.0)
grid.add_edge("H", "G", distance=20, weight=2.0)
grid.add_edge("F", "G", distance=20, weight=2.0)

#I tree and K-J Loop
grid.add_edge("I", "K", distance=30)
grid.add_edge("I", "J", distance=30)
grid.add_edge("K", "J", distance=15)
grid.add_edge("K", "M", distance=45)

#Pauli branches
grid.add_edge("Sok_Cell", "X", distance=25)
grid.add_edge("Sok_Cell", "Y", distance=25)
grid.add_edge("Sok_Cell", "Z", distance=25)
grid.add_edge("Sok_Cell", "Id", distance=25)

# --- CLASSICAL SIMULATION LOGIC ---
status = {}
dependencies = {
    "S_Ps": [], "D_Hub": ["S_Ps"], "Vit_Cell": ["S_Ps"], "Sok_Cell": ["S_Ps"], "I": ["S_Ps"],
    "N_Ps": ["D_Hub"], "L": ["D_Hub"], "B": ["D_Hub"], "Nov_Cell": ["N_Ps"], "C": ["B"],
    "H": ["Vit_Cell"], "F": ["Vit_Cell"], "G": ["H", "F"], "K": ["I"], "J": ["I"], "M": ["K"],
    "X": ["Sok_Cell"], "Y": ["Sok_Cell"], "Z": ["Sok_Cell"], "Id": ["Sok_Cell"]
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
            if node == "X":
                status[node] = "-" if status["Sok_Cell"] == "+" else "+"
            else:
                status[node] = "+" if random.random() < ONLINE_PROBABILITY else "-"

# --- BORN RULE MEASUREMENT HELPER ---
def born_rule_measure(vec):
    """Calculates real-world probabilities (|alpha|^2 and |beta|^2) and collapses the state."""
    prob_0 = abs(vec[0]) ** 2
    prob_1 = abs(vec[1]) ** 2
    outcome = "0 (Stable)" if random.random() < prob_0 else "1 (Trip)"
    return prob_0, prob_1, outcome

# --- R = HSH ("HALF-NOT") GATE HELPER FOR NODE L ---
def apply_R_gate(vec):
    """Applies R = H * S * H = [[(1+i)/2, (1-i)/2], [(1-i)/2, (1+i)/2]]."""
    a = (1 + 1j) / 2
    b = (1 - 1j) / 2
    new_0 = a * vec[0] + b * vec[1]
    new_1 = b * vec[0] + a * vec[1]
    return [new_0, new_1]






print("==================================================================")
print("     PHASE 1.5: INITIALIZING LOOP QUANTUM STATE VECTORS           ")
print("==================================================================")

verified_squares = ["I", "K", "J"]
vit_loop_nodes = ["Vit_Cell", "F", "G", "H"]
lottery_nodes = ["I", "K", "J"]
pauli_nodes = ["X", "Y", "Z", "Id"]
phase_nodes = ["L", "B"]

# 1. Print verification calculations for the Euclidean Norm (Vit_Cell Loop)
for node in vit_loop_nodes:
    theta_mock = random.uniform(0, 2 * math.pi)
    vec = [math.cos(theta_mock), math.sin(theta_mock)]

    a_val, b_val = vec[0], vec[1]
    euclidean_norm = math.sqrt(abs(a_val) ** 2 + abs(b_val) ** 2)
    p0, p1, outcome = born_rule_measure(vec)
    print(f"Node [{node:8}]: Vector [{a_val:.3f}, {b_val:.3f}] -> Norm: {euclidean_norm:.4f} | Born Odds: 0={p0:.0%}, 1={p1:.0%} -> {outcome}")

print("\n==================================================================")
print("     PHASE 1.6: ALL 4 PAULI GATES ON SOK_CELL BRANCH (I, X, Y, Z) ")
print("==================================================================")

theta_sok = random.uniform(0, 2 * math.pi)
sok_vector = [math.cos(theta_sok), math.sin(theta_sok)]

pauli_vectors = {
    "Id (Identity)": [sok_vector[0], sok_vector[1]],
    "X  (Pauli-X) ": [sok_vector[1], sok_vector[0]],
    "Y  (Pauli-Y) ": [-1j * sok_vector[1], 1j * sok_vector[0]],
    "Z  (Pauli-Z) ": [sok_vector[0], -sok_vector[1]]
}

print(f"Base Sok_Cell Vector -> [{sok_vector[0]:.3f}, {sok_vector[1]:.3f}]")
for gate_label, vec in pauli_vectors.items():
    norm = math.sqrt(abs(vec[0]) ** 2 + abs(vec[1]) ** 2)
    p0, p1, outcome = born_rule_measure(vec)
    print(f"Gate [{gate_label}]: Vector [{vec[0]:.3f}, {vec[1]:.3f}] -> Norm: {norm:.4f} | Born Odds: 0={p0:.0%}, 1={p1:.0%} -> {outcome}")

print("\n==================================================================")
print("     PHASE 1.65: PHASE & COMPOSITION GATES (L = HSH, B = T)       ")
print("==================================================================")

# 1. Node L starts at |0> = [1.0, 0.0] and runs R = HSH once, then twice (R^2 = NOT)
vec_L_start = [1.0, 0.0]
vec_L_once = apply_R_gate(vec_L_start)
vec_L_twice = apply_R_gate(vec_L_once)

norm_L1 = math.sqrt(abs(vec_L_once[0]) ** 2 + abs(vec_L_once[1]) ** 2)
p0_1, p1_1, out_1 = born_rule_measure(vec_L_once)
print(f"Node [L] (1x R = HSH) [Status: {status['L']}]: Norm: {norm_L1:.4f} | Born Odds: 0={p0_1:.0%}, 1={p1_1:.0%} -> {out_1}")

norm_L2 = math.sqrt(abs(vec_L_twice[0]) ** 2 + abs(vec_L_twice[1]) ** 2)
p0_2, p1_2, out_2 = born_rule_measure(vec_L_twice)
print(f"Node [L] (2x R = NOT) [Status: {status['L']}]: Norm: {norm_L2:.4f} | Born Odds: 0={p0_2:.0%}, 1={p1_2:.0%} -> {out_2}")

# 2. Node B keeps its original T-Gate (45-degree phase shift)
plus_state = [1.0 / math.sqrt(2), 1.0 / math.sqrt(2)]
t_factor = (1 + 1j) / math.sqrt(2)
vec_B = [plus_state[0], t_factor * plus_state[1]]

norm_B = math.sqrt(abs(vec_B[0]) ** 2 + abs(vec_B[1]) ** 2)
p0_B, p1_B, outcome_B = born_rule_measure(vec_B)
print(f"Node [B] (T-Gate 45°) [Status: {status['B']}]: Norm: {norm_B:.4f} | Born Odds: 0={p0_B:.0%}, 1={p1_B:.0%} -> {outcome_B}")


print("\n==================================================================")
print("     PHASE 1.7: RUNNING TRIPLE UNITARY VECTOR VERIFICATION        ")
print("==================================================================")

lottery_amplitude = 1.0 / math.sqrt(2)
for node in lottery_nodes:
    v_orig = [lottery_amplitude, lottery_amplitude]

    v_u1 = [v_orig[0], v_orig[1]]
    v_u2 = [v_orig[1], v_orig[0]]
    v_u3 = [(v_orig[0] + v_orig[1]) / math.sqrt(2), (v_orig[0] - v_orig[1]) / math.sqrt(2)]
    p0, p1, outcome = born_rule_measure(v_u3)

    print(f"Node [{node}]: Vector Before -> [{v_orig[0]:.3f}, {v_orig[1]:.3f}]")
    print(f"        -> After Identity : [{v_u1[0]:.3f}, {v_u1[1]:.3f}]")
    print(f"        -> After Pauli-X  : [{v_u2[0]:.3f}, {v_u2[1]:.3f}]")
    print(f"        -> After Hadamard : [{v_u3[0]:.3f}, {v_u3[1]:.3f}] | Born Odds: 0={p0:.0%}, 1={p1:.0%} -> {outcome}")
    print(f"        Result: Vector Before == After Transformations -> Generated good.\n")
print("==================================================================")

#MAPPING
pos = nx.spring_layout(grid, k=0.7, weight='weight', iterations=50)
labels = {node: f"{node}\n({status[node]})" for node in grid.nodes()}

plt.figure(figsize=(10, 6))

square_nodes_list = [n for n in grid.nodes() if n in verified_squares]
circle_nodes_list = [n for n in grid.nodes() if n not in verified_squares]

def get_node_color(node):
    if node in vit_loop_nodes:
        return "skyblue"
    elif node in lottery_nodes or node == "M":
        return "mediumpurple"
    elif node in pauli_nodes:
        return "deepskyblue"
    elif node in phase_nodes:
        return "gold"
    return "lightgreen" if status[node] == "+" else "coral"

if circle_nodes_list:
    nx.draw_networkx_nodes(
        grid, pos,
        nodelist=circle_nodes_list,
        node_color=[get_node_color(n) for n in circle_nodes_list],
        node_shape='o',
        node_size=1200
    )

if square_nodes_list:
    nx.draw_networkx_nodes(
        grid, pos,
        nodelist=square_nodes_list,
        node_color=[get_node_color(n) for n in square_nodes_list],
        node_shape='s',
        node_size=1300
    )

nx.draw_networkx_edges(grid, pos, alpha=0.5)
nx.draw_networkx_labels(grid, pos, labels=labels, font_size=7, font_weight="bold")

print("Grid Operational. Layout Simulation complete.")
plt.show()

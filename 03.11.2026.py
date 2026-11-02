import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator


#1. 3 qubits (one for each Last-End Node)
# Qubit 0 = Nov_Cell, Qubit 1 = Vit_Cell, Qubit 2 = Sok_Cell
qc = QuantumCircuit(3)

#2. Unitary Operation (Hadamard Gate) for Nov_Cell for it to be in a super position.
qc.h(0)

#3: Simulate a "dependancy" of one qubit onto another. only if novcell is good, we can make the vit cell good too
qc.cx(0, 1)


#4: Analyze the Quantum State Vector before measurement
#the third qubit remains unchanged, we don't use it yet.
state = Statevector.from_instruction(qc)
print("--- Quantum State Vector Topology ---")
print(state)
print("-------------------------------------")

#5: classical measurement gates
qc.measure_all()

#6: run
simulator = AerSimulator()
compiled_circuit = simulator.run(qc, shots=1024)
result = compiled_circuit.result()
counts = result.get_counts()
#actual results
print("\n Simulation Results (1024 Calculations):")
print(counts)

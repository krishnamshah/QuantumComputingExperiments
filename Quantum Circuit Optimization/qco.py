from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator

# Create a quantum circuit with redundant operations
qc = QuantumCircuit(1)

# Redundant operations
qc.h(0)
qc.h(0)
qc.x(0)
qc.x(0)

# Print the original circuit
print("Original Circuit:")
print(qc.draw())

# Optimize the circuit using Qiskit's transpiler with optimization level 3
optimized_qc = transpile(qc, AerSimulator(), optimization_level=3)

# Print the optimized circuit
print("\nOptimized Circuit:")
print(optimized_qc.draw())

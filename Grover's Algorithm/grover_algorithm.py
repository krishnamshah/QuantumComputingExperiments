
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import numpy as np

def oracle(circuit):
    circuit.cz(0, 1)  # CZ gate to mark the |11> state

def grover_diffuser(circuit):
    circuit.h([0, 1])
    circuit.z([0, 1])
    circuit.cz(0, 1)
    circuit.h([0, 1])

# Create a Quantum Circuit with 2 qubits and 2 classical bits
n = 2
qc = QuantumCircuit(n, n)

# Initialize the Circuit
qc.h([0, 1])

# Apply Grover's Algorithm
oracle(qc)
grover_diffuser(qc)

# Measure the qubits
qc.measure([0, 1], [0, 1])

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

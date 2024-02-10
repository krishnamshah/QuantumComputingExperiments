from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import numpy as np

# Create a quantum circuit with 2 qubits: 1 for the system, 1 for the ancilla
qc = QuantumCircuit(2, 1)

# Prepare the ancilla qubit in the |+> state
qc.h(0)

# Prepare the system qubit in an arbitrary state (e.g., |1>)
qc.x(1)

# Apply the controlled-U operation (U can be any unitary, here we use Z as an example)
qc.cz(0, 1)

# Apply a Hadamard gate to the ancilla qubit
qc.h(0)

# Measure the ancilla qubit
qc.measure(0, 0)

# Execute the circuit
simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)


from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Create a Quantum Circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to put the qubit in a superposition of |0> and |1>
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Simulate the circuit to generate a random number
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1)  # Only one shot needed
result = job.result()
counts = result.get_counts(qc)
print("Random Number:", counts)

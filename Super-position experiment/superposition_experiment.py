from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Create a Quantum Circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply the Hadamard gate to the qubit
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Use the Aer simulator to simulate the circuit
simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots=1024)  # Run the simulation 1024 times
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

# Optional: Visualize the results
plot_histogram(counts)

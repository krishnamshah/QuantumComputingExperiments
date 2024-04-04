from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Create a quantum circuit
qc = QuantumCircuit(1, 1)

# Apply X gate to the qubit
qc.x(0)

# Apply H gate to the qubit
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Execute the circuit
simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

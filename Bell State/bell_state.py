from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(2, 2)

# Create a Bell State
qc.h(0)
qc.cx(0, 1)

qc.measure([0, 1], [0, 1])

simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

# Optional: Visualize the results
# plot_histogram(counts)

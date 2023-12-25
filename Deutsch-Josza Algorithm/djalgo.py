from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Quantum Circuit with 3 qubits and 3 classical bits
n = 3
qc = QuantumCircuit(n + 1, n)

# Auxiliary Qubit
qc.x(n)

# Hadamard Gates
for qubit in range(n + 1):
    qc.h(qubit)

# CNOT gates
for qubit in range(n):
    qc.cx(qubit, n)

# Hadamard Gate
for qubit in range(n):
    qc.h(qubit)

# Measureing
for qubit in range(n):
    qc.measure(qubit, qubit)

simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots=1)  # Only one shot needed
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import numpy as np


def qft(circuit, n):
    """QFT on the first n qubits in circuit"""
    for i in range(n):
        for j in range(i):
            circuit.cp(np.pi / float(2 ** (i - j)), j, i)  # Apply Controlled-Phase gate
        circuit.h(i)


n = 3
qc = QuantumCircuit(n, n)

qc.x(0)  # Apply X gate to qubit 0
qc.h(1)  # Apply Hadamard gate to qubit 1

# Apply the QFT
qft(qc, n)

for i in range(n):
    qc.measure(i, i)


simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
import numpy as np

n = 3  # Number of qubits used for the phase register
qc = QuantumCircuit(n + 1, n)

qc.x(n)  # Apply X gate to the last qubit to prepare the state |1>
for qubit in range(n):
    qc.h(qubit)
repetitions = 1
for counting_qubit in range(n):
    for i in range(repetitions):
        qc.cp(np.pi, counting_qubit, n)  # Controlled-Pauli-X gate
    repetitions *= 2
qc.append(QFT(n).inverse(), range(n))
qc.measure(range(n), range(n))
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)
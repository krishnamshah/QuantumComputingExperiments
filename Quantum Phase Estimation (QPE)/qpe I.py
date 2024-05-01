from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_histogram
import numpy as np


def qpe(t, theta):
    qc = QuantumCircuit(t + 1, t)

    # Apply H gates to counting qubits
    for qubit in range(t):
        qc.h(qubit)

    # Prepare the eigenstate |psi> = U|0>
    qc.p(theta, t)

    # Apply controlled-U gates
    for counting_qubit in range(t):
        for _ in range(2**counting_qubit):
            qc.cp(theta, counting_qubit, t)

    # Apply inverse QFT
    qc.append(QFT(t).inverse(), range(t))

    # Measure counting qubits
    qc.measure(range(t), range(t))

    return qc


# Set the number of counting qubits and theta
t = 4
theta = 2 * np.pi * 0.5

qc = qpe(t, theta)

# Execute the circuit
backend = Aer.get_backend("qasm_simulator")
results = execute(qc, backend, shots=1000).result()
answer = results.get_counts()

# Print the result
print(answer)

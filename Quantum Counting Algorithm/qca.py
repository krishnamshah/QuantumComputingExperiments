from qiskit import QuantumCircuit, execute, Aer, transpile
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_histogram
import numpy as np


def grover_operator(qubits):
    # Grover's diffuser operator
    qc = QuantumCircuit(qubits)
    qc.h(range(qubits))
    qc.x(range(qubits))
    qc.h(qubits - 1)
    qc.mct(list(range(qubits - 1)), qubits - 1)  # Multi-controlled Toffoli
    qc.h(qubits - 1)
    qc.x(range(qubits))
    qc.h(range(qubits))
    return qc


def quantum_counting_circuit(qubits, marked_qubits):
    # Number of counting qubits
    counting_qubits = int(np.ceil(np.log2(qubits)))

    # Create Quantum Circuit
    qc = QuantumCircuit(qubits + counting_qubits, counting_qubits)

    # Initialize counting qubits in superposition
    qc.h(range(counting_qubits))

    # Apply Grover operator the appropriate number of times
    grover_op = grover_operator(marked_qubits)
    repetitions = 1
    for qubit in range(counting_qubits):
        for _ in range(repetitions):
            qc.append(grover_op, range(counting_qubits, qubits + counting_qubits))
        repetitions *= 2

    # Apply inverse Quantum Fourier Transform
    qc.append(QFT(counting_qubits, inverse=True), range(counting_qubits))

    # Measure the counting qubits
    qc.measure(range(counting_qubits), range(counting_qubits))

    return qc


# Set the number of qubits and marked qubits
n_qubits = 4
marked_qubits = 2

# Create and execute the quantum counting circuit
qc = quantum_counting_circuit(n_qubits, marked_qubits)
transpiled_qc = transpile(qc, Aer.get_backend("qasm_simulator"))
job = execute(transpiled_qc, Aer.get_backend("qasm_simulator"), shots=1024)
result = job.result()
counts = result.get_counts()

print("Measurement results:", counts)

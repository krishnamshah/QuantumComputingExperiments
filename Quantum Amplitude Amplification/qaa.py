from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import numpy as np


def amplitude_amplification_circuit(qubits):
    qc = QuantumCircuit(qubits)

    # Apply Hadamard gates to all qubits
    qc.h(range(qubits))

    # Oracle: Inverts the amplitude of a specific state (e.g., |11...1>)
    # For simplicity, let's consider the state |11...1>
    for qubit in range(qubits):
        qc.x(qubit)
    qc.h(qubits - 1)
    qc.mct(list(range(qubits - 1)), qubits - 1)  # Multi-controlled Toffoli
    qc.h(qubits - 1)
    for qubit in range(qubits):
        qc.x(qubit)

    # Amplification
    qc.h(range(qubits))
    for qubit in range(qubits):
        qc.x(qubit)
    qc.h(qubits - 1)
    qc.mct(list(range(qubits - 1)), qubits - 1)
    qc.h(qubits - 1)
    for qubit in range(qubits):
        qc.x(qubit)
    qc.h(range(qubits))

    return qc


# Number of qubits
n_qubits = 3

# Create the amplitude amplification circuit
qaa_circuit = amplitude_amplification_circuit(n_qubits)

# Add measurement
qaa_circuit.measure_all()

# Execute the circuit
simulator = Aer.get_backend("qasm_simulator")
job = execute(qaa_circuit, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qaa_circuit)
print("Measurement results:", counts)

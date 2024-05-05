from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import numpy as np

def initialize_walk(qc, total_qubits):
    """Initialize the quantum walk.
    Apply a Hadamard gate to the coin qubit to create a superposition of states.
    """
    qc.h(total_qubits - 1)

def step_walk(qc, total_qubits):
    """Perform one step of the quantum walk.
    Apply a conditional swap operation to shift the position of the walker,
    then apply a Hadamard gate to the coin qubit.
    """
    for i in range(total_qubits - 1):
        qc.cswap(total_qubits - 1, i, i + 1)
    qc.h(total_qubits - 1)

def quantum_walk(steps):
    """Perform a quantum walk of a given number of steps and return the resulting quantum circuit."""
    total_qubits = steps + 1
    qc = QuantumCircuit(total_qubits, steps)

    initialize_walk(qc, total_qubits)

    for _ in range(steps):
        step_walk(qc, total_qubits)

    qc.measure(list(range(steps)), list(range(steps)))

    return qc

def simulate_circuit(qc):
    """Simulate a quantum circuit and return the measurement counts."""
    simulator = Aer.get_backend("qasm_simulator")
    job = execute(qc, simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    return counts

def visualize_results(counts):
    """Visualize the results of a quantum walk using a histogram."""
    plot_histogram(counts)

# Perform a quantum walk of 3 steps
qc = quantum_walk(3)

# Simulate the quantum walk and get the measurement counts
counts = simulate_circuit(qc)

# Print the measurement results
print("Measurement results:", counts)

# Visualize the results
visualize_results(counts)
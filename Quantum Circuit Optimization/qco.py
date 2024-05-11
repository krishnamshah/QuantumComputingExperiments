from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator
from qiskit.circuit.random import random_circuit
import random


def optimize_circuit(qc):
    # Optimize the circuit using Qiskit's transpiler with optimization level 3
    optimized_qc = transpile(qc, AerSimulator(), optimization_level=3)
    return optimized_qc


def generate_and_optimize_random_circuit(n_qubits, depth):
    # Generate a random quantum circuit
    qc = random_circuit(n_qubits, depth, measure=True)

    # Print the original circuit
    print("Original Circuit:")
    print(qc.draw())

    # Optimize the circuit
    optimized_qc = optimize_circuit(qc)

    # Print the optimized circuit
    print("\nOptimized Circuit:")
    print(optimized_qc.draw())


# Generate and optimize a random circuit
n_qubits = random.randint(1, 5)  # Random number of qubits between 1 and 5
depth = random.randint(1, 5)  # Random depth between 1 and 5
generate_and_optimize_random_circuit(n_qubits, depth)

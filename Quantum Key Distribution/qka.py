from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import numpy as np
import random

# Parameters
n = 10  # Number of qubits used in the protocol

# Step 1: Alice generates a random bit string
alice_bits = [random.randint(0, 1) for _ in range(n)]

# Step 2: Alice generates a random basis for each bit
alice_bases = [random.randint(0, 1) for _ in range(n)]

# Step 3: Alice prepares qubits based on her bits and bases
qc = QuantumCircuit(n, n)
for i in range(n):
    if alice_bases[i] == 1:  # If the basis is 1, use the Hadamard basis
        qc.h(i)
    if alice_bits[i] == 1:  # Apply X gate if the bit is 1
        qc.x(i)
    qc.barrier()

# Step 4: Bob randomly chooses bases to measure each qubit
bob_bases = [random.randint(0, 1) for _ in range(n)]
for i in range(n):
    if (
        bob_bases[i] == 1
    ):  # If Bob's basis matches the Hadamard basis, apply H gate before measurement
        qc.h(i)
    qc.measure(i, i)

# Simulate the quantum circuit
simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots=1)
result = job.result()
measurements = result.get_counts(qc)

# Decode the measurement results
bob_bits = [int(bit) for bit in list(measurements.keys())[0]]

# Step 5: Alice and Bob publicly share their bases and keep bits where bases match
shared_bits = []
for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        shared_bits.append(bob_bits[i])

print("Shared secret key bits:", shared_bits)

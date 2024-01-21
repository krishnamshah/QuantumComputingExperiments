# Simon's Algorithm
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Define the secret string (change this to test different cases)
secret_string = "110"

# Create a quantum circuit with n qubits, where n is the length of the secret string
n = len(secret_string)
qc = QuantumCircuit(2 * n, n)

# Apply Hadamard gates to the first n qubits
for i in range(n):
    qc.h(i)

# Oracle: Apply CNOT gates based on the secret string
for i, s in enumerate(reversed(secret_string)):
    if s == '1':
        qc.cx(i, n + i)

# Apply Hadamard gates to the first n qubits again
for i in range(n):
    qc.h(i)

# Measure the first n qubits
qc.measure(range(n), range(n))

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

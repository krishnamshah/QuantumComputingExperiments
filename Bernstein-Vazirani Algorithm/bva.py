from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Define the secret string (you can change this to any binary string)
secret_string = "101"

# Create a quantum circuit with n+1 qubits (n qubits for the string, 1 auxiliary qubit)
n = len(secret_string)
qc = QuantumCircuit(n+1, n)

# Apply Hadamard gates before querying the oracle
qc.h(range(n))
qc.x(n)
qc.h(n)

# Oracle: Apply CX gates for each bit in the secret string that's 1
for i, bit in enumerate(reversed(secret_string)):
    if bit == '1':
        qc.cx(i, n)

# Apply Hadamard gates after querying the oracle
qc.h(range(n))

# Measure the first n qubits
qc.measure(range(n), range(n))

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

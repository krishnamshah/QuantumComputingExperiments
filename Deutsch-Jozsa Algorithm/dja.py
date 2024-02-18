from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Define the number of qubits for the oracle
n = 3  # Number of qubits used for the input to the oracle

# Create a quantum circuit with n qubits plus one for the oracle's output
qc = QuantumCircuit(n+1, n)

# Apply Hadamard gates before querying the oracle
for i in range(n):
    qc.h(i)

# Prepare the oracle's qubit in the state |->
qc.x(n)
qc.h(n)

# Define the oracle: Here we'll demonstrate with a balanced oracle
# For a constant oracle, you can omit the cx gates or ensure they do not change the parity of the input
for i in range(n):
    qc.cx(i, n)

# Apply Hadamard gates after querying the oracle
for i in range(n):
    qc.h(i)

# Measure the first n qubits
qc.measure(range(n), range(n))

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1)  # Only need one shot to determine the nature of the oracle
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

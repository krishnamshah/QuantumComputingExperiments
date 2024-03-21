from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Define the hidden binary string (adjust length as desired)
hidden_string = "10101"

# Create a quantum circuit with qubits equal to the length of the hidden string plus one ancilla qubit
qc = QuantumCircuit(len(hidden_string) + 1, len(hidden_string))

# Apply Hadamard gates to all qubits except the last ancilla qubit
for qubit in range(len(hidden_string)):
    qc.h(qubit)

# Prepare the ancilla qubit in the state |->
qc.x(len(hidden_string))
qc.h(len(hidden_string))

# Apply the oracle function: For each bit in the hidden string, apply a CNOT if the bit is 1
for i, bit in enumerate(hidden_string):
    if bit == "1":
        qc.cx(i, len(hidden_string))

# Apply Hadamard gates to all qubits except the ancilla qubit
for qubit in range(len(hidden_string)):
    qc.h(qubit)

# Measure the qubits to reveal the hidden string
qc.measure(range(len(hidden_string)), range(len(hidden_string)))

# Execute the circuit
simulator = Aer.get_backend("qasm_simulator")
job = execute(
    qc, simulator, shots=1
)  # Only need one shot due to the deterministic nature of the algorithm
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

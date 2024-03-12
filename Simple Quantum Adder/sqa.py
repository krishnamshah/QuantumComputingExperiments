from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 4 qubits and 2 classical bits for output
# qubits 0 and 1 will hold the numbers to be added
# qubit 2 will hold the carry bit
# qubit 3 will hold the sum bit
qc = QuantumCircuit(4, 2)

# Prepare the input states (|1⟩ + |1⟩)
qc.x(0)  # Set the first number to 1
qc.x(1)  # Set the second number to 1

# Perform the addition
qc.cx(0, 3)  # Perform a CNOT between qubit 0 and the sum bit (qubit 3)
qc.cx(1, 3)  # Perform a CNOT between qubit 1 and the sum bit (qubit 3)
qc.ccx(0, 1, 2)  # Perform a Toffoli gate to calculate the carry

# Measure the sum and carry
qc.measure(2, 0)  # Measure the carry bit into the first classical bit
qc.measure(3, 1)  # Measure the sum bit into the second classical bit

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

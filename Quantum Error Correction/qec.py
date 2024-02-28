from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a Quantum Circuit with 3 qubits for encoding, 2 for syndrome measurement, and 3 classical bits for the syndrome
qc = QuantumCircuit(5, 3)

# Prepare an arbitrary state for the first qubit
qc.x(0)  # Assuming the state |1> for demonstration; change as needed

# Encoding the state into a three-qubit entangled state
qc.cx(0, 1)
qc.cx(0, 2)

# Introduce an artificial bit-flip error on the second qubit
qc.x(1)  # Comment this out to see the effect of error correction when there's no error

# Syndrome measurement
qc.cx(0, 3)
qc.cx(1, 3)
qc.cx(1, 4)
qc.cx(2, 4)
qc.measure(3, 0)  # Measure the first ancilla qubit into the first classical bit
qc.measure(4, 1)  # Measure the second ancilla qubit into the second classical bit

# Correction based on the syndrome
qc.x(0).c_if(0b01, 1)  # If the syndrome is 01, flip the first qubit
qc.x(1).c_if(0b11, 1)  # If the syndrome is 11, flip the second qubit
qc.x(2).c_if(0b10, 1)  # If the syndrome is 10, flip the third qubit

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Syndrome measurement results:", counts)

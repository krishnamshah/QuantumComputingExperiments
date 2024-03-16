from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Initialize the circuit with 3 qubits and 2 ancilla qubits for parity checks
qc = QuantumCircuit(5, 2)

# Prepare an arbitrary state for demonstration
qc.x(0)  # Flip the first qubit to |1>

# Entangle the qubits to set up parity checks
qc.cx(0, 3)
qc.cx(1, 3)
qc.cx(1, 4)
qc.cx(2, 4)

# Introduce an artificial error (bit-flip) for demonstration
qc.x(1)  # Flip the second qubit

# Measure the parity qubits
qc.measure(3, 0)  # Measure the first ancilla qubit
qc.measure(4, 1)  # Measure the second ancilla qubit

# Execute the circuit on a simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

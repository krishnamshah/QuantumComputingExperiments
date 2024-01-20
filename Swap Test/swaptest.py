from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 3 qubits (2 for the states, 1 for the ancilla) and 1 classical bit
qc = QuantumCircuit(3, 1)

# Prepare the two quantum states you want to compare
# For this example, we'll compare |psi⟩ = |0⟩ and |phi⟩ = |1⟩
qc.x(1)  # Apply X gate to qubit 1 (|phi⟩)

# Apply a Hadamard gate to the ancilla qubit
qc.h(0)

# Controlled SWAP gate (Fredkin gate)
qc.cswap(0, 1, 2)

# Apply another Hadamard gate to the ancilla qubit
qc.h(0)

# Measure the ancilla qubit
qc.measure(0, 0)

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Apply a Hadamard gate to the control qubit (qubit 0) to put it into superposition
qc.h(0)

# Apply an X gate to the target qubit (qubit 1) to prepare it in the |1> state
qc.x(1)

# Apply a controlled-Z (CZ) operation from qubit 0 to qubit 1
qc.cz(0, 1)

# Apply another Hadamard gate to the control qubit
qc.h(0)

# Measure the control qubit
qc.measure_all()

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

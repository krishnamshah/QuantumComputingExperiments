from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector

# Create a Quantum Circuit with 3 qubits.
qc = QuantumCircuit(3,3)

# Apply X-gate to the first qubit
qc.x(0)

# Apply H-gate to the second qubit
qc.h(1)

# Apply CNOT-gate on the second and third qubit
qc.cx(1,2)

# Apply CNOT-gate on the first and second qubit
qc.cx(0,1)

# Apply H-gate to the first qubit
qc.h(0)

# Measure the first and second qubits
qc.measure([0,1],[0,1])

# Apply CNOT-gate on the second and third qubit
qc.cx(1,2)

# Apply CZ-gate on the first and third qubit
qc.cz(0,2)

# Measure the third qubit
qc.measure(2,2)

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
result = job.result()

# Print the result
counts = result.get_counts(qc)
print(counts)
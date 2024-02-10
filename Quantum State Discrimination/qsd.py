from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

# Define two non-orthogonal quantum states
state_0 = Statevector.from_label('0').data
state_1 = Statevector.from_instruction(QuantumCircuit(1).h(0)).data

# Create a quantum circuit to prepare and measure the state
qc = QuantumCircuit(1, 1)

# Assume we are given state_1 to discriminate
qc.initialize(state_1, 0)

# Measurement (no additional gates needed for this simple example)
qc.measure(0, 0)

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

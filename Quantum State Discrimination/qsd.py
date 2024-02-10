from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

# Define two non-orthogonal quantum states
state_0 = Statevector.from_label('0').data
state_1 = Statevector.from_instruction(QuantumCircuit(1).h(0)).data
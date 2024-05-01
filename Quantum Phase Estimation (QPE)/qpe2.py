from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.circuit.library import QFT
import numpy as np

def qpe(t, control_qubit, target_register):
    """Creates a QPE circuit"""
    qc = QuantumCircuit(t + 1, t)
    
    # Step 1: Prepare the quantum register
    qc.h(list(range(t)))
    qc.x(t)
    
    # Step 2: Apply controlled-U gates
    for qubit in range(t):
        qc.cp(2 * np.pi / 2**(t - qubit), qubit, t)
    
    # Step 3: Apply inverse QFT
    qc.append(QFT(t).inverse(), list(range(t)))
    
    # Step 4: Measure
    qc.measure(list(range(t)), list(range(t)))
    
    return qc

# Test the QPE algorithm
t = 3
control_qubit = 0
target_register = [1, 2, 3]
qpe_circuit = qpe(t, control_qubit, target_register)

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qpe_circuit, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qpe_circuit)
print("Counts:", counts)
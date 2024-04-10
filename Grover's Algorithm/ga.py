import numpy as np
import qiskit 
from qiskit import QuantumCircuit, transpile, Aer, execute

def grovers_algorithm(n,m,oracle):
    num_qubits = n
    num_states = m
    num_iterations = int((np.pi/4) / (np.arcsin(1/(2*math.sqrt(num_states))))**2)

    # Create the quantum circuit
    qc = QuantumCircuit(num_qubits, 0, 1)

    # Apply the oracle to mark the target state
    qc.apply_gate(oracle, range(num_qubits))
    
    # Invert the oracle to create a reflection
    qc.append([[oracle.inverse(), [i, j]] for i in range(num_qubits) for j in range(num_qubits)], [qr[i] for i in range(num_qubits)] + [cr[j] for j in range(num_states)])
    
    # Repeat the oracle application and its inverse (with a phase of -1) num_iterations times
    for i in range(num_iterations):
        qc.append([[oracle, [i, j]] for j in range(num_qubits)], [qr[j] for j in range(num_qubits)] + [cr[i] for i in range(num_states)])
        qc.append([[(oracle.inverse()), [i, j]] for j in range(num_qubits)], [qr[i] for i in range(num_qubits)] + [cr[num_states-1-j] for j in range(num_states)])
    
    # Measure the qubits to obtain the solution state
    qc.append([[(1, 0), [i, j]] for i in range(num_qubits) for j in range(num_qubits)], [qr[i] for i in range(num_qubits)] + [cr[j] for j in range(num_states)])
    
    # Execute the circuit on a simulator and obtain the result
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result()
    
    # Print the probability amplitude of the solution state
    counts = result.get_counts()
    print("Counts:", counts)

# Test the algorithm with 5 qubits and 3 marked states
num_qubits = 5
num_states = 3
oracle = None # Fill this in with an oracle for your specific problem
grovers_algorithm(num_qubits, num_states, oracle)
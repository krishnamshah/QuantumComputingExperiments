
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.visualization import plot_histogram

# Create Quantum Registers and Circuit
qr = QuantumRegister(3)  # Three qubits
cr = ClassicalRegister(2)  # Two classical bits
teleportation_circuit = QuantumCircuit(qr, cr)

# Step 1: Create Entanglement Between Two Qubits (q1 and q2)
teleportation_circuit.h(qr[1])  # Hadamard gate on q1
teleportation_circuit.cx(qr[1], qr[2])  # CNOT gate on q1 (control) and q2 (target)

# Step 2: Prepare the Initial State of the Qubit to be Teleported (q0)
teleportation_circuit.h(qr[0])  # State to be teleported

# Step 3: Perform Bell-state Measurement on the Qubits q0 and q1
teleportation_circuit.cx(qr[0], qr[1])
teleportation_circuit.h(qr[0])

# Step 4: Measure Qubits q0 and q1
teleportation_circuit.measure(qr[0], cr[0])
teleportation_circuit.measure(qr[1], cr[1])

# Step 5: Apply Correction Gates Based on the Measurement
teleportation_circuit.cz(qr[1], qr[2])
teleportation_circuit.cx(qr[0], qr[2])

# Simulate the Circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(teleportation_circuit, simulator, shots=1024)
result = job.result()
counts = result.get_counts(teleportation_circuit)
print("Measurement results:", counts)

from qiskit import QuantumCircuit, execute, Aer


def bernstein_vazirani(oracle, n):
    qc = QuantumCircuit(n + 1, n)

    # Initialize qubits
    for i in range(n):
        qc.h(i)
    qc.x(n)
    qc.h(n)

    # Apply the oracle
    qc += oracle

    # Apply Hadamard gates after the oracle
    for i in range(n):
        qc.h(i)

    # Measure the first n qubits
    qc.measure(range(n), range(n))

    # Execute the circuit
    backend = Aer.get_backend("qasm_simulator")
    result = execute(qc, backend, shots=1, memory=True).result()
    output = result.get_memory()[0]

    return output


# Define the oracle for a hidden integer
def hidden_integer_oracle(n, hidden_integer):
    qc = QuantumCircuit(n + 1)

    for qubit in range(n):
        if hidden_integer & (1 << qubit):
            qc.cx(qubit, n)

    oracle_gate = qc.to_gate()
    oracle_gate.name = "Oracle"

    return oracle_gate


n = 3
hidden_integer = 6
oracle = hidden_integer_oracle(n, hidden_integer)
print(bernstein_vazirani(oracle, n))

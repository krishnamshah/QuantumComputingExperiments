from qiskit import Aer, execute, QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.opflow import Z, I


# Define the ansatz circuit
def ansatz(theta):
    qc = QuantumCircuit(1)
    qc.rx(theta, 0)
    return qc


# Objective function to simulate the expectation value of Z for the ansatz state
def objective_function(theta):
    # Create a quantum circuit with the ansatz
    qc = ansatz(theta)

    # Use the operator Z to measure the expectation value
    observable = Z

    # Convert the circuit to an operator and evaluate the expectation value
    result = (~StateFn(observable) @ CircuitStateFn(qc)).eval()

    # Return the real part of the expectation value
    return np.real(result)


# Example usage
theta = Parameter("θ")
theta_val = np.pi / 4  # Example parameter value

# Simulate the expectation value
expectation_value = objective_function(theta_val)
print("Expectation Value:", expectation_value)

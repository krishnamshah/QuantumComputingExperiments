from qiskit import Aer, execute, QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.optimization.applications.ising import max_cut
from qiskit.aqua.algorithms import NumPyMinimumEigensolver
from qiskit.optimization.applications.ising.common import sample_most_likely
from qiskit.aqua.operators import Z, X, I, CircuitStateFn, PauliExpectation, StateFn
from qiskit.aqua.operators.gradients import Gradient
import numpy as np

# Define the graph for the Max-Cut problem
edges = [(0, 1)]


# Define the QAOA circuit
def qaoa_circuit(beta, gamma):
    n_qubits = 2
    qc = QuantumCircuit(n_qubits)
    # Initial state
    for i in range(n_qubits):
        qc.h(i)
    # Problem unitary
    for edge in edges:
        i, j = edge
        qc.rzz(2 * gamma, i, j)
    # Mixer unitary
    for i in range(n_qubits):
        qc.rx(2 * beta, i)
    return qc


# Objective function
def objective_function(params):
    beta, gamma = params
    qc = qaoa_circuit(beta, gamma)
    op = PauliExpectation().convert(
        ~StateFn(Z ^ Z) @ CircuitStateFn(primitive=qc, coeff=1.0)
    )
    result = op.eval()
    return np.real(result)


# Example parameters
params = np.array([np.pi / 4, np.pi / 4])

# Find the minimum eigenvalue
optimizer = GradientDescent()
opt_result = optimizer.optimize(
    num_vars=2, objective_function=objective_function, initial_point=params
)

# Print optimized parameters and result
print("Optimized Parameters:", opt_result[0])
print("Minimum Eigenvalue:", opt_result[1])

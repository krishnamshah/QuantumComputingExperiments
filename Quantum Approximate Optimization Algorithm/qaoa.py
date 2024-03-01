from qiskit import Aer, execute, QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.opflow import (
    Z,
    X,
    I,
    StateFn,
    PauliExpectation,
    CircuitSampler,
    AerPauliExpectation,
)
from qiskit.utils import QuantumInstance
from qiskit.algorithms.optimizers import COBYLA
import numpy as np

# Define a simple Max-Cut problem
edges = [(0, 1)]


# Define the QAOA circuit
def qaoa_circuit(beta, gamma):
    n_qubits = 2
    qc = QuantumCircuit(n_qubits)
    # Initial state
    for i in range(n_qubits):
        qc.h(i)
    # Problem unitary
    for i, j in edges:
        qc.rzz(2 * gamma, i, j)
    # Mixer unitary
    for i in range(n_qubits):
        qc.rx(2 * beta, i)
    return qc


# Objective function for QAOA
def objective_function(params):
    backend = Aer.get_backend("statevector_simulator")
    qi = QuantumInstance(backend)
    beta, gamma = params
    qc = qaoa_circuit(beta, gamma)
    op = Z ^ Z  # Max-Cut Hamiltonian for a 2-node graph
    expectation = StateFn(op, is_measurement=True) @ StateFn(qc)
    sampler = CircuitSampler(qi).convert(expectation)
    value = sampler.eval().real
    return value


# Optimizer
optimizer = COBYLA()

# Initial parameters
params = np.array([np.pi / 4, np.pi / 4])

# Optimization
result = optimizer.optimize(
    num_vars=2, objective_function=objective_function, initial_point=params
)

print("Optimized Parameters:", result[0])
print("Minimum Value:", result[1])

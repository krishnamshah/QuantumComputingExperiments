from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import VQE
from qiskit.algorithms.optimizers import COBYLA
from qiskit.circuit.library import TwoLocal
from qiskit.opflow import PauliSumOp
from qiskit.quantum_info import Pauli
import numpy as np

# Define the Hamiltonian in the Pauli basis
pauli_dict = {
    'II': -1.052373245772859,
    'IZ': 0.39793742484318045,
    'ZI': -0.39793742484318045,
    'ZZ': -0.01128010425623538,
    'XX': 0.18093119978423156
}

qubit_op = PauliSumOp.from_list([(Pauli(label), coeff) for label, coeff in pauli_dict.items()])

# Define the quantum instance
seed = 50
quantum_instance = QuantumInstance(Aer.get_backend('statevector_simulator'), seed_transpiler=seed, seed_simulator=seed)

# Define the variational form (ansatz)
var_form = TwoLocal(qubit_op.num_qubits, ['ry', 'rz'], 'cz', reps=3)

# Define the classical optimizer
optimizer = COBYLA(maxiter=500)

# Run VQE
vqe = VQE(ansatz=var_form, optimizer=optimizer, quantum_instance=quantum_instance)
result = vqe.compute_minimum_eigenvalue(qubit_op)

print('The ground state energy is: {}'.format(result.eigenvalue.real))
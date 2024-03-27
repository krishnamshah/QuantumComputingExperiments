from qiskit import QuantumCircuit, assemble, execute, Aer, transpile
from qiskit.visualization import plot_histogram
from qiskit.algorithms import Shor
from qiskit.circuit.library import qft_dagger

def shor(N):
    qc = QuantumCircuit(4*N + 2, 2*N)
    for qubit in range(2*N):
        qc.h(qubit)
    qc.x(4*N)
    for counting_qubit in range(2*N):
        for i in range(2**(2*N -1 - counting_qubit)):
            qc.unitary(Shor.c_amod15(a, 2**(2*N -1 - counting_qubit)), 
                       [counting_qubit] + [i+n for n in range(3*N + 1)], label='U')
    qc.append(qft_dagger(2*N), range(2*N))
    qc.measure(range(2*N), range(2*N))
    return qc

qc = shor(15)
qasm_sim = Aer.get_backend('qasm_simulator')
t_qc = transpile(qc, qasm_sim)
qobj = assemble(t_qc)
results = qasm_sim.run(qobj).result()
counts = results.get_counts()
plot_histogram(counts)
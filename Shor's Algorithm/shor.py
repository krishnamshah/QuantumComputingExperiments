from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT  # Import QFT from the new location


def qpe_amod15(a, power):
    qc = QuantumCircuit(4 + len(power), 4)
    for j in range(power):
        qc.h(j)
    qc.x(3 + power)
    for repeat in range(power):
        qc.append(c_amod15(a, 2**repeat), [repeat] + [i + power for i in range(4)])
    qc.append(QFT(power).inverse(), list(range(power)))  # Use QFT from the new location
    qc.measure(list(range(power)), list(range(power)))
    return qc


qc = qpe_amod15(7, 8)
simulator = Aer.get_backend("qasm_simulator")
counts = execute(qc, backend=simulator, shots=1024).result().get_counts()
plot_histogram(counts)

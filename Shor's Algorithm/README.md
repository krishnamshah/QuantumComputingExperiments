# Shor's Algorithm Experiment

## Overview
Shor's Algorithm is a quantum algorithm for integer factorization. It's one of the most famous quantum algorithms due to its potential impact on cryptography.

## Running the Program
This program requires Python and Qiskit. It constructs a quantum circuit to implement Shor's Algorithm for factoring the number 15.

### Procedure:
1. **Initialization**: Create a quantum circuit with qubits corresponding to the length of the number to be factored, plus ancilla qubits.
2. **Oracle Application**: Implement the oracle function using controlled modular multiplication gates.
3. **Algorithm Execution**: Apply Hadamard gates, perform Quantum Fourier Transform, perform measurements, and execute the circuit to reveal the factors.

## Understanding the Results
The output of the circuit will reveal the factors of the number. This algorithm's efficiency contrasts with classical algorithms, which require exponential time to factor large numbers.

## Significance
Shor's Algorithm demonstrates the potential of quantum computing to solve problems that are infeasible for classical computers, with significant implications for cryptography and security.
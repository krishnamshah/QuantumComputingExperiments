# Advanced Bernstein-Vazirani Algorithm Experiment

## Overview
The Bernstein-Vazirani Algorithm showcases the power of quantum computing by solving a problem more efficiently than classical computers. Given a black box oracle function that hides a binary string, this algorithm identifies the string in a single query, regardless of its length.

## Running the Program
This program requires Python and Qiskit. It constructs a quantum oracle encoding a hidden binary string, then applies the Bernstein-Vazirani algorithm to determine the string with one quantum query.

### Procedure:
1. **Initialization**: Create a quantum circuit with qubits corresponding to the length of the hidden string, plus an ancilla qubit.
2. **Oracle Application**: Implement the oracle function using CNOT gates based on the hidden string.
3. **Algorithm Execution**: Apply Hadamard gates, perform measurements, and execute the circuit to reveal the hidden string.

## Understanding the Results
The output of the circuit will directly reveal the hidden binary string encoded in the oracle. This single-query efficiency contrasts with classical algorithms, which require a number of queries proportional to the string length.

## Significance
Demonstrating superior efficiency in specific tasks, the Bernstein-Vazirani Algorithm is a cornerstone in understanding quantum algorithms' potential and their implications for computing and information theory.

# Simple Quantum Adder Experiment

## Overview
A quantum adder is a fundamental component in quantum computing, illustrating how basic arithmetic operations can be performed on a quantum computer. This example demonstrates a simple quantum circuit designed to add two single-qubit numbers, showcasing the principles of quantum logic gates and superposition in computational tasks.

## Running the Program
To run this experiment, ensure you have Python and Qiskit installed. The program creates a quantum circuit to add two single-qubit numbers using quantum gates, and then measures the output to observe the result of the addition.

### Steps:
1. **Prepare Inputs**: The circuit initializes two qubits to represent the numbers to be added.
2. **Addition Logic**: Utilizes CNOT and Toffoli gates to perform the addition and calculate the carry bit.
3. **Measurement**: The sum and carry are measured, translating the quantum information into classical to interpret the result.

## Understanding the Results
The output of the program illustrates the result of adding two qubits. For the input |1⟩ + |1⟩, the expected output demonstrates the calculation of the sum and carry bits, reflecting the basic operation of a quantum adder.

## Significance
Understanding quantum adders is crucial for building more complex quantum algorithms and arithmetic operations, serving as a stepping stone towards full-fledged quantum computing applications.

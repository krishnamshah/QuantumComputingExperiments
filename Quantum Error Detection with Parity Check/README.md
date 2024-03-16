# Quantum Error Detection with Parity Check

## Overview
Quantum Error Detection using Parity Check codes is a fundamental strategy for identifying errors in quantum systems. This approach leverages ancilla (helper) qubits to measure the parity of subsets of qubits, allowing for the detection of single bit-flip errors without directly measuring the state of the system qubits.

## Running the Program
Ensure you have Python and Qiskit installed. This program demonstrates a basic quantum error detection scheme on a three-qubit system using two ancilla qubits for parity checks. It introduces a controlled error to illustrate how the error can be detected through parity measurements.

### Steps:
1. **State Preparation**: An arbitrary state is prepared for demonstration purposes.
2. **Parity Check Setup**: Qubits are entangled with ancilla qubits to set up parity checks.
3. **Error Introduction**: A bit-flip error is artificially introduced to one of the qubits.
4. **Error Detection**: The ancilla qubits are measured to detect the error based on parity.

## Understanding the Results
The measurement results of the ancilla qubits indicate whether an error has occurred and on which part of the system, based on the parity outcomes. This technique allows for error detection without collapsing the quantum state of the system qubits.

## Significance
Quantum Error Detection and Correction are crucial for the development of reliable quantum computing, as they protect against errors due to decoherence and quantum noise, ensuring the integrity of quantum information.

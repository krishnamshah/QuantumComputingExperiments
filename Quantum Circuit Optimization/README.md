# Quantum Circuit Optimization

## Overview
Quantum Circuit Optimization is a critical process in quantum computing that aims to reduce the number of quantum gates, minimize circuit depth, and eliminate redundancies. This process is essential for enhancing the performance of quantum algorithms, especially given the constraints of current quantum hardware, such as gate errors and limited coherence times.

## Running the Program
This example demonstrates a simple circuit optimization technique using Qiskit's `transpile` function. The program starts with a quantum circuit that includes redundant operations and applies Qiskit's built-in optimization tools to simplify the circuit.

### Prerequisites:
- Ensure you have Python and Qiskit installed in your environment. If not, you can install Qiskit using pip:

```bash
pip install qiskit
```
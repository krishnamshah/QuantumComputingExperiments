# Three-Qubit Bit-Flip Error Correction Code Experiment

## Overview
Quantum Error Correction (QEC) is essential for protecting quantum information against environmental noise and errors during computation. This program demonstrates the three-qubit bit-flip code, a simple QEC code that corrects single bit-flip errors.

## Running the Program
To run this experiment, ensure Python and Qiskit are installed. The program encodes a quantum bit into an entangled state of three qubits, introduces an error, performs syndrome measurement to detect the error, and corrects it.

## Understanding the Results
The syndrome measurement results indicate which qubit experienced a bit-flip error. The correction operation is applied conditionally based on the syndrome, demonstrating how QEC codes can identify and correct errors to preserve quantum information.

# BB84 Protocol for Quantum Key Distribution

## Overview
The BB84 protocol is a quantum key distribution scheme developed by Charles Bennett and Gilles Brassard in 1984. It allows two parties, traditionally named Alice and Bob, to establish a shared secret key, even in the presence of an eavesdropper. The security of the protocol is based on the principles of quantum mechanics.

## Running the Program
Ensure Python and Qiskit are installed. This program simulates the BB84 protocol, where Alice sends qubits to Bob, who measures them in randomly chosen bases. Alice and Bob then compare their bases and keep the bits where their bases match to form a shared secret key.

### Steps:
1. **Random Bit Generation**: Alice generates a random bit string.
2. **Basis Selection**: Alice and Bob randomly choose bases for preparation and measurement.
3. **Qubit Preparation and Measurement**: Alice prepares qubits based on her bits and bases, and Bob measures them in his bases.
4. **Basis Comparison**: Alice and Bob publicly share their bases and discard bits where their bases do not match.
5. **Key Formation**: The remaining bits form the shared secret key.

## Understanding the Results
The output of the program is a shared secret key known only to Alice and Bob, provided there is no eavesdropper. The security of the key relies on the no-cloning theorem and the fact that measurements in quantum mechanics are intrusive.

## Significance
QKD protocols like BB84 are crucial for achieving secure communication in the era of quantum computing and potentially safeguarding against future quantum attacks.

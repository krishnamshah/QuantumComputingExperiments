

# Quantum Computing Experiments

Welcome to Quantum Computing Experiments! This repository is dedicated to exploring fundamental quantum algorithms and concepts through practical coding examples. Our primary focus is on demonstrating basic principles of quantum computing to those new to the field or interested in its applications.

## About the Project

Quantum computing harnesses the unique behavior of quantum physics, such as superposition, entanglement, and quantum interference, to perform computations. It holds the potential to solve certain problems much faster than classical computers.

### Current Experiments

1. **Superposition and Measurement**: Demonstrates the quantum principle of superposition using a Hadamard gate.
2. **Deutsch-Josza Algorithm**: Implements the Deutsch-Josza algorithm to showcase the efficiency of quantum algorithms.
3. **Bell State**: Creates and measures a Bell State, demonstrating the concept of quantum entanglement.
4. **Quantum Fourier Transform (QFT)**: Implements the Quantum Fourier Transform, a key component in many quantum algorithms.
5. **Quantum Teleportation**: Demonstrates the teleportation of a qubit's state using quantum entanglement and classical communication.
6. **Quantum Random Number Generator (QRNG)**: Generates truly random numbers by exploiting the inherent randomness of quantum mechanics.


## Getting Started

### Prerequisites

- **Python**: A recent version of Python (3.7 or newer) is required.
- **Qiskit**: We use Qiskit, an open-source quantum computing framework by IBM. Install it using pip:
  ```bash
  pip install qiskit
  ```

```bash
pip install pip-tools
pip-compile deploy/requirements.in
pip install -r deploy/requirements.txt
```  

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/krishnamshah/QuantumComputingExperiments.git
```

Navigate to the cloned directory:

```bash
cd QuantumComputingExperiments
```

This experiment is crucial for understanding quantum parallelism and interference.

## Contributing

Contributions to expand or improve the experiments are welcome! 

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Thanks to the Qiskit community and IBM for their extensive resources on quantum computing.




# Quantum Computing Experiments

Welcome to Quantum Computing Experiments! This repository is dedicated to exploring fundamental quantum algorithms and concepts through practical coding examples. Our primary focus is on demonstrating basic principles of quantum computing to those new to the field or interested in its applications.

## About the Project

Quantum computing harnesses the unique behavior of quantum physics, such as superposition, entanglement, and quantum interference, to perform computations. It holds the potential to solve certain problems much faster than classical computers.

### Current Experiments

- **Superposition and Measurement**: A simple demonstration of quantum superposition using a Hadamard gate.
- **Deutsch-Josza Algorithm**: An implementation of the Deutsch-Josza algorithm, showcasing the efficiency of quantum algorithms for specific problems.

## Getting Started

### Prerequisites

- **Python**: A recent version of Python (3.7 or newer) is required.
- **Qiskit**: We use Qiskit, an open-source quantum computing framework by IBM. Install it using pip:
  ```bash
  pip install qiskit
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

## Experiments

### Superposition and Measurement

This experiment demonstrates the concept of superposition. A qubit is placed in a superposition state using a Hadamard gate, and then measured. The outcome is probabilistic, showcasing one of the fundamental principles of quantum mechanics.

### Deutsch-Josza Algorithm

The Deutsch-Josza algorithm is one of the earliest examples demonstrating the power of quantum computers. It can determine whether a given function is constant or balanced (outputting an equal number of 0s and 1s) in a single evaluation - a task impossible for classical computers to achieve with the same efficiency.

#### Understanding the Results

- If the algorithm outputs all 0s, the function is constant.
- If there is at least one 1, the function is balanced.

This experiment is crucial for understanding quantum parallelism and interference.

## Contributing

Contributions to expand or improve the experiments are welcome! 

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Thanks to the Qiskit community and IBM for their extensive resources on quantum computing.
- Special thanks to all contributors who have helped to make this project educational and insightful.


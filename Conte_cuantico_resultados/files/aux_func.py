from qiskit import QuantumCircuit, QuantumRegister, Aer, execute, ClassicalRegister
from qiskit.visualization import plot_histogram
import numpy as np

def calculate_solutions(a, n, p):
    theta = 2 * np.pi * (a / 2**(p + 1))
    return 2**n * np.sin(theta)**2

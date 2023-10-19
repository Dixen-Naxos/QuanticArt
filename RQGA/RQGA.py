from qiskit import *
from collections import Counter
import numpy as np


def ia(size):
    ia_mat = 2 * np.ones(size) / size
    ia_mat = ia_mat - np.identity(size)
    return ia_mat


def oracle(size, val_array):
    _oracle = np.identity(size)
    for val in val_array:
        _oracle[val][val] = -1
    return _oracle


def rqga(current_val):
    n = 6
    predictions = 10000

    circuit = QuantumCircuit(n)
    circuit.h(range(n))
    rand_theta = np.random.uniform(0, 2 * np.pi / n, n)
    for i in range(n):
        circuit.rz(rand_theta[i], i)

    GIM = ia(2 ** n)

    circuit.unitary(oracle(2**n, [current_val]), range(n), label='Oracle')
    circuit.unitary(GIM, range(n), label='Grover Inv')

    circuit.measure_all()

    sim = Aer.get_backend('qasm_simulator')
    result = execute(circuit, backend=sim, shots=predictions).result().get_counts()

    return max(result)
    #return average(result, predictions)


def average(result, predictions):
    sum = 0

    for key in result.keys():
        sum += (result[key] - int(predictions * 0.4) // len(result)) * int(key, 2)

    return sum // int(predictions * 0.6)


def max(result):
    max_key = next(iter(result.keys()))

    for key in result.keys():
        if result[key] > result[max_key]:
            max_key = key

    return int(max_key, 2)
